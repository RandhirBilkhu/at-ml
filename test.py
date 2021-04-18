import pandas as pd


df = read.csv("winequality-red.csv")

quality_mapping ={
    4:0,
    5:1,
    6:2,
    3:3,
    7:4,
    8:5
}