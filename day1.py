from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def datasets_demo():
    """
    sklearn 数据集的使用
    :return:
    """
    # import datasets
    iris = load_iris()
    print("iris\n", iris)  # print iris
    print("iris.DESCR\n", iris[DESCR])  # iris.DESCR
    print("iris.feature_names\n", iris.feature_names)  # iris.feature_names
    print("iris.data\n", iris.data, iris.data.shape)  # print iris.data and iris.data.shape

    return None


if __name__ == "__main__":
    datasets_demo()
