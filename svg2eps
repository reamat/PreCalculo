#!/bin/bash

for i in $(find  -name '*.svg'); do
  arq_eps="${i%.svg}.eps"
  if ! [ -f $arq_eps ];
  then
    echo $i "->" $arq_eps
    inkscape -f $i -E $arq_eps
  fi
done
