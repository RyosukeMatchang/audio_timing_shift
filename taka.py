import pandas as pd 
from kl_set import calculate_kl_divergence_sum, count_topic_tag_proportions

def _validate_set(df, num_sample_per_set, reference_prob, kl_threshold1):
    ok_set_id_list = []
    for set_id in df['set_id'].unique():
        df_sub = df[df['set_id'] == set_id]

        # check the number of samples
        if len(df_sub) != num_sample_per_set: 
            continue    
        # check the number of unique files
        if df_sub["filename"].nunique() != num_sample_per_set: 
            continue
        # check the KL divergence
        partial_prob = count_topic_tag_proportions(df_sub)
        if calculate_kl_divergence_sum(reference_prob, partial_prob) > kl_threshold1:
            continue

        ok_set_id_list.append(set_id)

    return ok_set_id_list


def assign_set(
    df_org: pd.DataFrame,
    reference_prob: dict,
    kl_threshold1: float,
    num_sample_per_delay: 2,
    num_trial: int = 1000,
):
    df = df_org.copy()

    # extract delay value from filename
    df['delay_value'] = df['filename'].str.extract(r'delay([\-]?\d+\.\d+)')[0].astype(float)
    delay_value_list = df['delay_value'].unique()
    assert len(delay_value_list) % num_sample_per_delay == 0, 'The number of samples must be a multiple of num_sample_per_delay.'

    df["set_id"] = None
    num_sample_per_set = num_sample_per_delay * len(delay_value_list)
    num_set = len(df) // num_sample_per_set
    set_id_list = [f"set{i+1}" for i in range(num_set)]

    n_trial = 0
    num_remaining_list = []
    while df["set_id"].isnull().any():
        df_loop = df[df["set_id"].isnull()].sample(frac=1)

        # assign set_id for each delay value
        for delay in delay_value_list:   
            _df = df_loop[df_loop['delay_value'] == delay]

            for idx in range(len(_df) // num_sample_per_delay):
                df.loc[_df.index[idx*num_sample_per_delay:(idx+1)*num_sample_per_delay], "set_id"] = set_id_list[idx]

        # validate set (True if the set is valid)
        ok_set_id_list = _validate_set(
            df, num_sample_per_set, reference_prob, kl_threshold1)

        # remove invalid set_id
        df["set_id"] = df["set_id"].apply(lambda x: x if x in ok_set_id_list else None)
        set_id_list = list(set(set_id_list) - set(ok_set_id_list))
        num_remaining_list.append(len(df[df['set_id'].isnull()]))

        print(f"{n_trial}-th trial: {num_remaining_list[-1]} / {len(df)}")
 
        n_trial += 1
        if n_trial > num_trial:
            print("The number of trials has reached the limit. Stop the process.")
            break

        if len(num_remaining_list) > 10:
            if all([num_remaining_list[i] == num_remaining_list[-1] for i in range(-10, 0)]):
                print("The number of remaining samples is not decreasing. Stop the process.")
                break

    return df

# load data
df_all = pd.read_csv('comment_list.csv')

# statistics of total data
reference_prob = count_topic_tag_proportions(df_all)
df_sub = df_all.copy()

# assign set_id
df = assign_set(
    df_sub, reference_prob=reference_prob, 
    kl_threshold1=0.18, num_sample_per_delay=2)
df.to_csv('comment_list_with_set_id.csv', index=False)
