
import pickle
pickle.dump(None, open('test.pkl', 'wb'))

print(pickle.load(open('test.pkl', 'rb')))
