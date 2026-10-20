import matplotlib
matplotlib.use("Agg")
import matplotlib as plt
import numpy as np
import json


data_for_bts={}
data_for_valuelearning={}
data_for_qlearning={}


def saving():
    with open ("Documentation.json") as f:
        data_for_bts= json.open(f)["bts"]
        data_for_valuelearning = json.open(f)["value_learning"]
        data_for_qlearning = json.open(f)["q_learning"]


def plotting():
    plt.plot(data_for_bts.keys(), data_for_bts.values()["reward"], color="red", label="reward per episode of bts")

    plt.plot(data_for_valuelearning.keys(), data_for_valuelearning.values()["reward"], color ="green", label="reward per episode of value learning")

    plt.plot(data_for_qlearning(), data_for_qlearning.values()["reward"], color ="blue", label="reward per episode of q learning")

    plt.xlabel("episode"); plt.ylabel("reward"); plt.legend()

    plt.savefig("curve.png", dpi=500)

    print("saved curve.png")


def do_all():
    saving()
    plotting()