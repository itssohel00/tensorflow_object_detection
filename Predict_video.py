from tensorflow.keras.models import load_model
import cv2
import numpy as np
import statistics

#model = load_model("ResNet50_model_weights(old).h5")

model = load_model("ResNet50_model_weights_B8_L64.h5")

#model = load_model("ResNet50_model_weights(with_val)1024.h5")
#left cornar all box3, box2 70%

#model = load_model("ResNet50_model_weights(without_val)1024.h5")
#box2 0%
#model = load_model("ResNet50_model_weights(without_val)512.h5")
#model = load_model("ResNet50_model_weights(without_val)256.h5")
#model = load_model("ResNet50_model_weights_B8_L32.h5")
#000


CATEGORIES = ["box1", "box2", "box3", "box4", "nothing"]

def prepare(image):
    IMG_SIZE = 150  # in txt-based
    new_array = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)

##############

cap = cv2.VideoCapture(0)

# カメラ設定
result = "---"
prediction2 = "---"
final_p = "---"
p_list = []

while(True):
    ret, frame = cap.read()

    # 画面のメッセージ  
    cv2.putText(frame, 'Press D for  Detection, Press Q to Quit', (135, 50), cv2.FONT_ITALIC, 0.5, (255,255,255))  
    cv2.putText(frame, prediction2, (20, 40), cv2.FONT_ITALIC, 1.0, (0,0,250))
    # グレー化
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    img_infer = frame
    pre_img = prepare(img_infer)
    prediction = model.predict(pre_img)
        
    #print(prediction) # will be a list in a list.
    b = prediction[0]
    c = b.tolist()
    #print ("Max value element : ", c.index(max(c)))
    prediction2 = (CATEGORIES[int(c.index(max(c)))])
    #print(prediction2)

    if prediction2 != 'nothing':
        p_list.append(c.index(max(c)))
    else:
        if len(p_list) > 15:
            try:
                index_p = statistics.mode(p_list)
            except:
                print('Undefine')
            else:
                #print(p_list)
                final_p = (CATEGORIES[int(index_p)])
                count_p = p_list.count(index_p)
                persentage_p = count_p/len(p_list)*100
                print(final_p)
                print(persentage_p)
                #if persentage_p >= 50:            
                    #print(final_p)
                #else:
                    #print('Undefine')
                p_list = []
        #p_list2 = p_list[:len(p_list)-1]
        """if len(p_list) != 0:
            index_p = statistics.mode(p_list)
            final_p = (CATEGORIES[int(index_p)])
            if final_p != 'nothing':
                count_p = p_list.count(index_p)
                persentage_p = count_p/len(p_list)*100
                if persentage_p >= 80:            
                    print(final_p)
                else:
                    print('Undefine')
                                    
                p_list = []"""
    
    

    # One Short prediction
    """if cv2.waitKey(20) & 0xFF == ord('d'):  
        img_infer = frame
        pre_img = prepare(img_infer)
        prediction = model.predict(pre_img)
        
        #print(prediction) # will be a list in a list.
        b = prediction[0]
        c = b.tolist()
        #print ("Max value element : ", c.index(max(c)))
        prediction2 = (CATEGORIES[int(c.index(max(c)))])
        #print(prediction2)

        if prediction2 != 'nothing':             
            p_list.append(c.index(max(c)))
            
        if len(p_list) == 10:            
            #print(p_list)
            index_p = statistics.mode(p_list)
            count_p = p_list.count(index_p)
            persentage_p = count_p/len(p_list)*100
            if persentage_p >= 80:
                final_p = (CATEGORIES[int(index_p)])
                print(final_p)
            else:
                print('Undefine')
                            
            p_list = []"""
        

        
        #result =  prediction2
        #print(prediction2)
        

    # カメラ開始
    cv2.imshow('frame', frame)

    # カメラを閉じる（Q）
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# カメラ解放
cap.release()
cv2.destroyAllWindows()

