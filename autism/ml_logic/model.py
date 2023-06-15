from tensorflow.keras.models import load_model

def load_local_model(path='autism/ml_logic/Alex_model/'):
    '''loads model saved on a local drive'''
    model = load_model(path)
    return model

if __name__ == "__main__":
    model = load_local_model()
    print(model)
