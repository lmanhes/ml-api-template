

class BadassModel(object):

    def __init__(self, from_s3=True):
        if from_s3:
            # load ml artifacts from s3
            pass
        else:
            # load ml artifacts from local dir
            pass

    def predict(self, feat_1, feat_2, feat_3, name):
        return f'Hey {name}, the result is {sum([feat_1, feat_2, feat_3])}'