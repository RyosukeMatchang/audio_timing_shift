#!/bin/bash

# FF1からFF8までコピー
for i in {1..8}; do
    cp add_prefix.sh "../FF$i"
done

# MF11からMF18までコピー
for i in {11..18}; do
    cp add_prefix.sh "../MF$i"
done

# MF21からMF28までコピー
for i in {21..28}; do
    cp add_prefix.sh "../MF$i"
done

# MM1からMM8までコピー
for i in {1..8}; do
    cp add_prefix.sh "../MM$i"
done
