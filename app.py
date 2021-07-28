# Importing essential libraries
from flask import Flask, render_template, request , Markup
import pandas as pd
import pickle
import numpy as np
from math import floor

# Load the model

filename = 'E:\mini\House Data\Bengaluru_house.pkl'
model = pickle.load(open(filename, 'rb'))
X = pd.read_csv('E:\mini\House data\Bengaluru1.csv', index_col=0)

app = Flask(__name__)


def predict_priced(location,size,total_sqft,bath,balcony,area_type):
    loc_index, area_index = -1,-1
    
    
    if location!='Rest of Bangalore':
        loc_index = int(np.where(X.columns==location)[0][0])
    
    if area_type!='Super built-up  Area':
        area_index = np.where(X.columns==area_type)[0][0]
        
    x=np.zeros(len(X.columns))
    x[0] = size
    x[1] = total_sqft
    x[2] = bath
    x[3] = balcony
    
    
    if loc_index >=0:
        x[loc_index] = 1
        
    if area_index >= 0:
        x[area_index] = 1
    return model.predict([x])[0]

predict_priced('1st Block Jayanagar',2,1000,2,1,'Built-up  Area')


@app.route('/')
def home():
    locality = ('1st Block Jayanagar' , '1st Phase JP Nagar' ,"2nd Phase Judicial Layout" , "2nd Stage Nagarbhavi" , "5th Block Hbr Layout" , "5th Phase JP Nagar",
                "6th Phase JP Nagar","7th Phase JP Nagar","8th Phase JP Nagar","9th Phase JP Nagar","AECS Layout","Abbigere","Akshaya Nagar","Ambalipura",
                "Ambedkar Nagar","Amruthahalli","Anandapura","Ananth Nagar","Anekal","Anjanapura","Ardendale","Arekere","Attibele","BEML Layout","BTM 2nd Stage",
                "BTM Layout","Babusapalaya","Badavala Nagar","Balagere","Banashankari","Banashankari Stage II","Banashankari Stage III","Banashankari Stage V",
                "Banashankari Stage VI","Banaswadi","Banjara Layout","Bannerghatta","Bannerghatta Road","Basavangudi","Basaveshwara Nagar","Battarahalli",
                "Begur","Begur Road","Bellandur","Benson Town","Bharathi Nagar","Bhoganhalli","Billekahalli","Binny Pete","Bisuvanahalli","Bommanahalli",
                "Bommasandra","Bommasandra Industrial Area","Bommenahalli","Brookefield","Budigere","CV Raman Nagar","Chamrajpet","Chandapura","Channasandra",
                "Chikka Tirupathi","Chikkabanavar","Chikkalasandra","Choodasandra","Cooke Town","Cox Town","Cunningham Road","Dasanapura","Dasarahalli",
                "Devanahalli","Devarachikkanahalli","Dodda Nekkundi","Doddaballapur","Doddakallasandra","Doddathoguru","Domlur","Dommasandra","EPIP Zone",
                "Electronic City","Electronic City Phase II","Electronics City Phase 1","Frazer Town","GM Palaya","Garudachar Palya","Giri Nagar",
                "Gollarapalya Hosahalli","Gottigere","Green Glen Layout","Gubbalala","Gunjur","HAL 2nd Stage","HBR Layout","HRBR Layout","HSR Layout",
                "Haralur Road","Harlur","Hebbal","Hebbal Kempapura","Hegde Nagar","Hennur","Hennur Road","Hoodi","Horamavu Agara","Horamavu Banaswadi",
                "Hormavu","Hosa Road","Hosakerehalli","Hoskote","Hosur Road","Hulimavu","ISRO Layout","ITPL","Iblur Village","Indira Nagar","JP Nagar",
                "Jakkur","Jalahalli","Jalahalli East","Jigani","Judicial Layout","KR Puram","Kadubeesanahalli","Kadugodi","Kaggadasapura","Kaggalipura",
                "Kaikondrahalli","Kalena Agrahara","Kalyan nagar","Kambipura","Kammanahalli","Kammasandra","Kanakapura","Kanakpura Road","Kannamangala",
                "Karuna Nagar","Kasavanhalli","Kasturi Nagar","Kathriguppe","Kaval Byrasandra","Kenchenahalli","Kengeri","Kengeri Satellite Town",
                "Kereguddadahalli","Kodichikkanahalli","Kodigehaali","Kodigehalli","Kodihalli","Kogilu","Konanakunte","Koramangala","Kothannur","Kothanur",
                "Kudlu","Kudlu Gate","Kumaraswami Layout","Kundalahalli","LB Shastri Nagar","Laggere","Lakshminarayana Pura","Lingadheeranahalli",
                "Magadi Road","Mahadevpura","Mahalakshmi Layout","Mallasandra","Malleshpalya","Malleshwaram","Marathahalli","Margondanahalli","Marsur",
                "Mico Layout","Munnekollal","Murugeshpalya","Mysore Road","NGR Layout","NRI Layout","Nagarbhavi","Nagasandra","Nagavara","Nagavarapalya",
                "Narayanapura","Neeladri Nagar","Nehru Nagar","OMBR Layout","Old Airport Road","Old Madras Road","Padmanabhanagar","Pai Layout","Panathur",
                "Parappana Agrahara","Pattandur Agrahara","Poorna Pragna Layout","Prithvi Layout","R.T. Nagar","Rachenahalli","Raja Rajeshwari Nagar",
                "Rajaji Nagar","Rajiv Nagar","Ramagondanahalli","Ramamurthy Nagar","Rayasandra","Sahakara Nagar","Sanjay nagar","Sarakki Nagar","Sarjapur",
                "Sarjapur  Road","Sarjapura - Attibele Road","Sector 2 HSR Layout","Sector 7 HSR Layout","Seegehalli","Shampura","Shivaji Nagar","Singasandra",
                "Somasundara Palya","Sompura","Sonnenahalli","Subramanyapura","Sultan Palaya","TC Palaya","Talaghattapura","Thanisandra","Thigalarapalya","Thubarahalli",
                "Tindlu","Tumkur Road","Ulsoor","Uttarahalli","Varthur","Varthur Road","Vasanthapura","Vidyaranyapura","Vijayanagar","Vishveshwarya Layout",
                "Vishwapriya Layout","Vittasandra","Whitefield","Yelachenahalli","Yelahanka","Yelahanka New Town","Yelenahalli","Yeshwanthpur" )
    
    _area_type = ["Built-up  Area" , "Carpet  Area" ,"Plot  Area"]
    return render_template('front.html' , localities =locality , area_types = _area_type) 

@app.route('/', methods=['POST'])
def predict():
    if request.method == 'POST':
        location = str(request.form['Location'])
        size = int(request.form['BHK'])
        bath = int(request.form['Bathroom'])
        balcony = int(request.form['Balcony'])
        total_sqft = int(request.form['Sq feet'])
        area_type = str(request.form['Area Type'])        
        predicted = predict_priced(location,size,total_sqft,bath,balcony,area_type)
        
        return render_template('result.html', prediction = floor(predicted))

if __name__ == '__main__':
	 app.run(debug=True)