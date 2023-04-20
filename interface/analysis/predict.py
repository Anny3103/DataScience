import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor


class Model:
    def __init__(self):
        self.model = self.train_model()

    def train_model(self):
        Data_natural = pd.read_excel('data/Data_natural.xlsx')
        # Выделим зависимую переменную
        Y = Data_natural['Прибыль в расчете на 1 работника']
        # DataFrame не содержащий целевой признак
        X_ALL = Data_natural.drop('Прибыль в расчете на 1 работника', axis=1)
        # Разбиваем датасет на train/test исходные данные без стандартизации
        X_train, X_test, y_train, y_test = train_test_split(X_ALL, Y, train_size=0.8, test_size=0.2, random_state=0)
        # модель регрессии GradientBoostingRegressor
        X_train = X_train.set_axis(['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12'], axis=1)
        X_test = X_test.set_axis(['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12'], axis=1)
        model_HGB = HistGradientBoostingRegressor(max_depth=5, max_leaf_nodes=9)
        model_HGB.fit(X_train, y_train)

        return model_HGB

    def pred(self, x_data):
        return self.model.predict(x_data)


