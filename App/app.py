{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "XnOIvEhWC4X0"
   },
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "FSO4pxwpC6Qk"
   },
   "source": [
    "**ChatBot 1.0**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ocU0yDCvC2WU",
    "outputId": "f926bc0b-ddcb-40cf-d24c-9030b686d828"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: nltk in /usr/local/lib/python3.7/dist-packages (3.2.5)\n",
      "Requirement already satisfied: six in /usr/local/lib/python3.7/dist-packages (from nltk) (1.15.0)\n"
     ]
    }
   ],
   "source": [
    "pip install nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "L2kh10r-DINb",
    "outputId": "7135e6b7-1336-4c33-98f5-2e905a63b7d6"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting newspaper3k\n",
      "  Downloading newspaper3k-0.2.8-py3-none-any.whl (211 kB)\n",
      "\u001b[?25l\r",
      "\u001b[K     |█▌                              | 10 kB 18.1 MB/s eta 0:00:01\r",
      "\u001b[K     |███                             | 20 kB 23.0 MB/s eta 0:00:01\r",
      "\u001b[K     |████▋                           | 30 kB 26.5 MB/s eta 0:00:01\r",
      "\u001b[K     |██████▏                         | 40 kB 27.9 MB/s eta 0:00:01\r",
      "\u001b[K     |███████▊                        | 51 kB 30.2 MB/s eta 0:00:01\r",
      "\u001b[K     |█████████▎                      | 61 kB 33.4 MB/s eta 0:00:01\r",
      "\u001b[K     |██████████▉                     | 71 kB 33.8 MB/s eta 0:00:01\r",
      "\u001b[K     |████████████▍                   | 81 kB 34.7 MB/s eta 0:00:01\r",
      "\u001b[K     |██████████████                  | 92 kB 36.7 MB/s eta 0:00:01\r",
      "\u001b[K     |███████████████▌                | 102 kB 31.1 MB/s eta 0:00:01\r",
      "\u001b[K     |█████████████████               | 112 kB 31.1 MB/s eta 0:00:01\r",
      "\u001b[K     |██████████████████▋             | 122 kB 31.1 MB/s eta 0:00:01\r",
      "\u001b[K     |████████████████████▏           | 133 kB 31.1 MB/s eta 0:00:01\r",
      "\u001b[K     |█████████████████████▊          | 143 kB 31.1 MB/s eta 0:00:01\r",
      "\u001b[K     |███████████████████████▎        | 153 kB 31.1 MB/s eta 0:00:01\r",
      "\u001b[K     |████████████████████████▉       | 163 kB 31.1 MB/s eta 0:00:01\r",
      "\u001b[K     |██████████████████████████▍     | 174 kB 31.1 MB/s eta 0:00:01\r",
      "\u001b[K     |████████████████████████████    | 184 kB 31.1 MB/s eta 0:00:01\r",
      "\u001b[K     |█████████████████████████████▌  | 194 kB 31.1 MB/s eta 0:00:01\r",
      "\u001b[K     |███████████████████████████████ | 204 kB 31.1 MB/s eta 0:00:01\r",
      "\u001b[K     |████████████████████████████████| 211 kB 31.1 MB/s \n",
      "\u001b[?25hCollecting tldextract>=2.0.1\n",
      "  Downloading tldextract-3.1.2-py2.py3-none-any.whl (87 kB)\n",
      "\u001b[?25l\r",
      "\u001b[K     |███▊                            | 10 kB 26.6 MB/s eta 0:00:01\r",
      "\u001b[K     |███████▌                        | 20 kB 33.9 MB/s eta 0:00:01\r",
      "\u001b[K     |███████████▎                    | 30 kB 43.1 MB/s eta 0:00:01\r",
      "\u001b[K     |███████████████                 | 40 kB 49.5 MB/s eta 0:00:01\r",
      "\u001b[K     |██████████████████▉             | 51 kB 52.5 MB/s eta 0:00:01\r",
      "\u001b[K     |██████████████████████▋         | 61 kB 57.2 MB/s eta 0:00:01\r",
      "\u001b[K     |██████████████████████████▍     | 71 kB 59.5 MB/s eta 0:00:01\r",
      "\u001b[K     |██████████████████████████████  | 81 kB 62.2 MB/s eta 0:00:01\r",
      "\u001b[K     |████████████████████████████████| 87 kB 6.9 MB/s \n",
      "\u001b[?25hCollecting jieba3k>=0.35.1\n",
      "  Downloading jieba3k-0.35.1.zip (7.4 MB)\n",
      "\u001b[K     |████████████████████████████████| 7.4 MB 35.0 MB/s \n",
      "\u001b[?25hCollecting tinysegmenter==0.3\n",
      "  Downloading tinysegmenter-0.3.tar.gz (16 kB)\n",
      "Collecting feedparser>=5.2.1\n",
      "  Downloading feedparser-6.0.8-py3-none-any.whl (81 kB)\n",
      "\u001b[K     |████████████████████████████████| 81 kB 9.0 MB/s \n",
      "\u001b[?25hRequirement already satisfied: python-dateutil>=2.5.3 in /usr/local/lib/python3.7/dist-packages (from newspaper3k) (2.8.2)\n",
      "Requirement already satisfied: lxml>=3.6.0 in /usr/local/lib/python3.7/dist-packages (from newspaper3k) (4.2.6)\n",
      "Requirement already satisfied: requests>=2.10.0 in /usr/local/lib/python3.7/dist-packages (from newspaper3k) (2.23.0)\n",
      "Collecting cssselect>=0.9.2\n",
      "  Downloading cssselect-1.1.0-py2.py3-none-any.whl (16 kB)\n",
      "Requirement already satisfied: beautifulsoup4>=4.4.1 in /usr/local/lib/python3.7/dist-packages (from newspaper3k) (4.6.3)\n",
      "Requirement already satisfied: nltk>=3.2.1 in /usr/local/lib/python3.7/dist-packages (from newspaper3k) (3.2.5)\n",
      "Requirement already satisfied: PyYAML>=3.11 in /usr/local/lib/python3.7/dist-packages (from newspaper3k) (3.13)\n",
      "Collecting feedfinder2>=0.0.4\n",
      "  Downloading feedfinder2-0.0.4.tar.gz (3.3 kB)\n",
      "Requirement already satisfied: Pillow>=3.3.0 in /usr/local/lib/python3.7/dist-packages (from newspaper3k) (7.1.2)\n",
      "Requirement already satisfied: six in /usr/local/lib/python3.7/dist-packages (from feedfinder2>=0.0.4->newspaper3k) (1.15.0)\n",
      "Collecting sgmllib3k\n",
      "  Downloading sgmllib3k-1.0.0.tar.gz (5.8 kB)\n",
      "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests>=2.10.0->newspaper3k) (1.24.3)\n",
      "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests>=2.10.0->newspaper3k) (3.0.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests>=2.10.0->newspaper3k) (2021.5.30)\n",
      "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests>=2.10.0->newspaper3k) (2.10)\n",
      "Requirement already satisfied: filelock>=3.0.8 in /usr/local/lib/python3.7/dist-packages (from tldextract>=2.0.1->newspaper3k) (3.0.12)\n",
      "Collecting requests-file>=1.4\n",
      "  Downloading requests_file-1.5.1-py2.py3-none-any.whl (3.7 kB)\n",
      "Building wheels for collected packages: tinysegmenter, feedfinder2, jieba3k, sgmllib3k\n",
      "  Building wheel for tinysegmenter (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
      "  Created wheel for tinysegmenter: filename=tinysegmenter-0.3-py3-none-any.whl size=13552 sha256=3a7764762d7081c748def76ec668a3f82c51e35f091064dbe56f32a834fb974f\n",
      "  Stored in directory: /root/.cache/pip/wheels/df/67/41/faca10fa501ca010be41b49d40360c2959e1c4f09bcbfa37fa\n",
      "  Building wheel for feedfinder2 (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
      "  Created wheel for feedfinder2: filename=feedfinder2-0.0.4-py3-none-any.whl size=3356 sha256=b68c8dbc991dc755b0890c833a6be0e18d3686298731caccc4512e092f9c9510\n",
      "  Stored in directory: /root/.cache/pip/wheels/7f/d4/8f/6e2ca54744c9d7292d88ddb8d42876bcdab5e6d84a21c10346\n",
      "  Building wheel for jieba3k (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
      "  Created wheel for jieba3k: filename=jieba3k-0.35.1-py3-none-any.whl size=7398405 sha256=a14f36943d23c02cd3aed1c89d26998f12bac382a097d8772e65ed053e154918\n",
      "  Stored in directory: /root/.cache/pip/wheels/4c/91/46/3c208287b726df325a5979574324878b679116e4baae1af3c3\n",
      "  Building wheel for sgmllib3k (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
      "  Created wheel for sgmllib3k: filename=sgmllib3k-1.0.0-py3-none-any.whl size=6065 sha256=60d8ce0e960b1708df434330b4bb180a9e8f7525414ce787327f26b95ec55ee1\n",
      "  Stored in directory: /root/.cache/pip/wheels/73/ad/a4/0dff4a6ef231fc0dfa12ffbac2a36cebfdddfe059f50e019aa\n",
      "Successfully built tinysegmenter feedfinder2 jieba3k sgmllib3k\n",
      "Installing collected packages: sgmllib3k, requests-file, tldextract, tinysegmenter, jieba3k, feedparser, feedfinder2, cssselect, newspaper3k\n",
      "Successfully installed cssselect-1.1.0 feedfinder2-0.0.4 feedparser-6.0.8 jieba3k-0.35.1 newspaper3k-0.2.8 requests-file-1.5.1 sgmllib3k-1.0.0 tinysegmenter-0.3 tldextract-3.1.2\n"
     ]
    }
   ],
   "source": [
    "pip install newspaper3k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "jIwb1qldDf6v"
   },
   "outputs": [],
   "source": [
    "#import the libraries\n",
    "from newspaper import Article\n",
    "import random\n",
    "import string\n",
    "import nltk\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "import numpy as np\n",
    "import warnings \n",
    "warnings.filterwarnings('ignore')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ktR1CXxPEHWi",
    "outputId": "3af59643-8de9-432f-bf92-f19fb2845e4f"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#download the punkt package\n",
    "nltk.download('punkt', quiet=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "kVsGbMhSEKVY"
   },
   "outputs": [],
   "source": [
    "#Get the unicef article\n",
    "article = Article('https://www.unicef.org/india/coronavirus/covid-19') \n",
    "article.download()\n",
    "article.parse()\n",
    "article.nlp()\n",
    "corpus = article.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "k3kLYk2uEwN5",
    "outputId": "1ced0ec8-c669-4709-bc3e-35b3220aeb80"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Should I wear a mask?\n",
      "\n",
      "The use of a mask is advised to protect others even if you have no symptoms.\n",
      "\n",
      "\n",
      "\n",
      "After masks are worn, they must be used and disposed of properly to ensure their effectiveness and to avoid any increased risk of transmitting the virus.\n",
      "\n",
      "The use of a mask alone is not enough to stop infections and must be combined with frequent hand washing with soap and maintaining physical distance.\n",
      "\n",
      "Does COVID-19 affect children?\n",
      "\n",
      "COVID-19 is a new virus, and we are still learning about how it affects children and pregnant women. We know people of any age can be infected and transmit the virus. However, older people and/or those with pre-existing medical conditions seem more likely to develop severe illness. Cold, mild cough, fever, and body pain are the common symptoms of infection. We have also noted that other symptoms such as pain in the abdomen, loose motions, and vomiting are also present in children.\n",
      "\n",
      "Clinical features or symptoms affecting children and adolescents, possibly associated with COVID-19, can include but are not limited to: fever, headache, body pain, tiredness, cough, breathlessness, poor feeding, loss of taste or smell (in a child more than eight years old), rash, red or pink eyes, swollen and/or red lips, tongue, hands, feet, gastrointestinal problems (diarrhoea, vomiting).\n",
      "\n",
      "\n",
      "\n",
      "What should I do if my child has symptoms of COVID-19 or has been in contact with someone who has tested positive?\n",
      "\n",
      "Seek medical attention. If advised by the doctor, then get your child tested for COVID-19. If advised by a doctor isolate/stay home.\n",
      "\n",
      "Record temperature and oxygen saturation with a pulse oximeter if available at home, every 6 hours. Measure their temperature frequently. If it is more than 100-degree F, then you can do tepid sponging with tap water and give them syrup or tablet paracetamol. If fever is >100°F, give paracetamol 10–15 mg/kg/dose.\n",
      "\n",
      "\n",
      "\n",
      "Continue to follow good hand and respiratory hygiene practices like regular handwashing with soap so that your child is protected against other viruses and bacteria causing diseases.\n",
      "\n",
      "\n",
      "\n",
      "Continue to follow personal protective measures for yourself and your child. Your child should wear a surgical mask anytime they are around people. Change the mask after eight hours of continuous wear. Caregivers interacting with the child should wear gloves and a mask.\n",
      "\n",
      "\n",
      "\n",
      "Feed your child home-cooked food and keep them well hydrated. Give plenty of liquids and give a soft and light diet. One may give vitamin C, zinc to boost overall health and immunity\n",
      "\n",
      "\n",
      "\n",
      "Other nutritional supplements like syrup multivitamin, Vitamin C, vitamin D, calcium can be given as per their doctor’s advice.\n",
      "\n",
      "\n",
      "\n",
      "Be watchful for danger signs and if any of these signs are present, seek urgent medical advice at your nearest hospital.\n",
      "\n",
      "\n",
      "\n",
      "Indrawing of chest\n",
      "\n",
      "Grunting sounds\n",
      "\n",
      "The child looks pale or blue\n",
      "\n",
      "Peripheries feel cold\n",
      "\n",
      "Sunken eyeballs and dry mouth\n",
      "\n",
      "Not passed urine for more than 3- 4 hours (for children less than 5 years of age)\n",
      "\n",
      "Refusing to feed\n",
      "\n",
      "Looks drowsy or lethargic\n",
      "\n",
      "Abnormal body movement\n",
      "\n",
      "Severe diarrhea, vomiting or abdominal pain.\n",
      "\n",
      "What is the best way to wash hands properly?\n",
      "\n",
      "Step 1:Wet hands with running water\n",
      "\n",
      "Step 2: Apply enough soap to cover wet hands\n",
      "\n",
      "Step 3: Scrub all surfaces of the hands – including back of hands, between fingers and under nails – for at least 20 seconds\n",
      "\n",
      "Step 4: Rinse thoroughly with running water\n",
      "\n",
      "Step 5: Dry hands with a clean cloth or single-use towel\n",
      "\n",
      "\n",
      "\n",
      "Wash your hands often, especially before eating; after blowing your nose, coughing, or sneezing; and going to the bathroom.\n",
      "\n",
      "\n",
      "\n",
      "If soap and water are not readily available, use an alcohol-based hand sanitizer with at least 60% alcohol. Always wash hands with soap and water, if hands are visibly dirty.\n",
      "\n",
      "What precautions should I take for my family if we travel?\n",
      "\n",
      "Anyone planning a trip overseas should always check the travel advisory for their destination country for any restrictions on entry, quarantine requirements on entry, or other relevant travel advice.\n",
      "\n",
      "In addition to taking standard travel precautions, and in order to avoid being quarantined or denied re-entry into your home country, you are also advised to check the latest COVID-19 update on the International Air Transport Association website, which includes a list of countries and restriction measures.\n",
      "\n",
      "While traveling, all parents should follow standard hygiene measures for themselves and their children: Wash hands frequently or use an alcohol-based sanitizer with at least 60 per cent alcohol, practice good respiratory hygiene (cover your mouth and nose with your bent elbow or tissue when you cough or sneeze and immediately dispose of the used tissue) and avoid close contact with anyone who is coughing or sneezing.\n",
      "\n",
      "\n",
      "\n",
      "In addition, it is recommended that parents always carry a hand sanitizer, pack of disposable tissues, and disinfecting wipes.\n",
      "\n",
      "Additional recommendations include: Clean your seat, armrest, touchscreen, etc. with a disinfecting wipe once inside an aircraft or other vehicle. Also use a disinfecting wipe to clean key surfaces, doorknobs, remote controls, etc at the hotel or other accommodation where you and your children are staying.\n",
      "\n",
      "Can pregnant women pass coronavirus to unborn children?\n",
      "\n",
      "At this time, there is not enough evidence to determine whether the virus is transmitted from a mother to her baby during pregnancy, or the potential impact this may have on the baby. This is currently being investigated. Pregnant women should continue to follow appropriate precautions to protect themselves from exposure to the virus, and seek medical care early, if experiencing symptoms, such as fever, cough or difficulty breathing.\n",
      "\n",
      "Is it safe for a mother to breastfeed if she is infected with coronavirus?\n",
      "\n",
      "All mothers in affected and at-risk areas who have symptoms of fever, cough or difficulty breathing, should seek medical care early, and follow instructions from a health care provider.\n",
      "\n",
      "Considering the benefits of breastfeeding and the insignificant role of breastmilk in the transmission of other respiratory viruses, the mother can continue breastfeeding, while applying all the necessary precautions.\n",
      "\n",
      "For symptomatic mothers well enough to breastfeed, this includes wearing a mask when near a child (including during feeding), washing hands before and after contact with the child (including feeding), and cleaning/disinfecting contaminated surfaces – as should be done in all cases where anyone with confirmed or suspected COVID-19 interacts with others, including children.\n",
      "\n",
      "If a mother is too ill, she should be encouraged to express milk and give it to the child via a clean cup and/or spoon – all while following the same infection prevention methods.\n"
     ]
    }
   ],
   "source": [
    "#print the article text\n",
    "print(corpus)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "PkrzxrPHE9Oc",
    "outputId": "87c115a2-cfcc-4bd6-cec4-37b46d12e3a1"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Should I wear a mask?', 'The use of a mask is advised to protect others even if you have no symptoms.', 'After masks are worn, they must be used and disposed of properly to ensure their effectiveness and to avoid any increased risk of transmitting the virus.', 'The use of a mask alone is not enough to stop infections and must be combined with frequent hand washing with soap and maintaining physical distance.', 'Does COVID-19 affect children?', 'COVID-19 is a new virus, and we are still learning about how it affects children and pregnant women.', 'We know people of any age can be infected and transmit the virus.', 'However, older people and/or those with pre-existing medical conditions seem more likely to develop severe illness.', 'Cold, mild cough, fever, and body pain are the common symptoms of infection.', 'We have also noted that other symptoms such as pain in the abdomen, loose motions, and vomiting are also present in children.', 'Clinical features or symptoms affecting children and adolescents, possibly associated with COVID-19, can include but are not limited to: fever, headache, body pain, tiredness, cough, breathlessness, poor feeding, loss of taste or smell (in a child more than eight years old), rash, red or pink eyes, swollen and/or red lips, tongue, hands, feet, gastrointestinal problems (diarrhoea, vomiting).', 'What should I do if my child has symptoms of COVID-19 or has been in contact with someone who has tested positive?', 'Seek medical attention.', 'If advised by the doctor, then get your child tested for COVID-19.', 'If advised by a doctor isolate/stay home.', 'Record temperature and oxygen saturation with a pulse oximeter if available at home, every 6 hours.', 'Measure their temperature frequently.', 'If it is more than 100-degree F, then you can do tepid sponging with tap water and give them syrup or tablet paracetamol.', 'If fever is >100°F, give paracetamol 10–15 mg/kg/dose.', 'Continue to follow good hand and respiratory hygiene practices like regular handwashing with soap so that your child is protected against other viruses and bacteria causing diseases.', 'Continue to follow personal protective measures for yourself and your child.', 'Your child should wear a surgical mask anytime they are around people.', 'Change the mask after eight hours of continuous wear.', 'Caregivers interacting with the child should wear gloves and a mask.', 'Feed your child home-cooked food and keep them well hydrated.', 'Give plenty of liquids and give a soft and light diet.', 'One may give vitamin C, zinc to boost overall health and immunity\\n\\n\\n\\nOther nutritional supplements like syrup multivitamin, Vitamin C, vitamin D, calcium can be given as per their doctor’s advice.', 'Be watchful for danger signs and if any of these signs are present, seek urgent medical advice at your nearest hospital.', 'Indrawing of chest\\n\\nGrunting sounds\\n\\nThe child looks pale or blue\\n\\nPeripheries feel cold\\n\\nSunken eyeballs and dry mouth\\n\\nNot passed urine for more than 3- 4 hours (for children less than 5 years of age)\\n\\nRefusing to feed\\n\\nLooks drowsy or lethargic\\n\\nAbnormal body movement\\n\\nSevere diarrhea, vomiting or abdominal pain.', 'What is the best way to wash hands properly?', 'Step 1:Wet hands with running water\\n\\nStep 2: Apply enough soap to cover wet hands\\n\\nStep 3: Scrub all surfaces of the hands – including back of hands, between fingers and under nails – for at least 20 seconds\\n\\nStep 4: Rinse thoroughly with running water\\n\\nStep 5: Dry hands with a clean cloth or single-use towel\\n\\n\\n\\nWash your hands often, especially before eating; after blowing your nose, coughing, or sneezing; and going to the bathroom.', 'If soap and water are not readily available, use an alcohol-based hand sanitizer with at least 60% alcohol.', 'Always wash hands with soap and water, if hands are visibly dirty.', 'What precautions should I take for my family if we travel?', 'Anyone planning a trip overseas should always check the travel advisory for their destination country for any restrictions on entry, quarantine requirements on entry, or other relevant travel advice.', 'In addition to taking standard travel precautions, and in order to avoid being quarantined or denied re-entry into your home country, you are also advised to check the latest COVID-19 update on the International Air Transport Association website, which includes a list of countries and restriction measures.', 'While traveling, all parents should follow standard hygiene measures for themselves and their children: Wash hands frequently or use an alcohol-based sanitizer with at least 60 per cent alcohol, practice good respiratory hygiene (cover your mouth and nose with your bent elbow or tissue when you cough or sneeze and immediately dispose of the used tissue) and avoid close contact with anyone who is coughing or sneezing.', 'In addition, it is recommended that parents always carry a hand sanitizer, pack of disposable tissues, and disinfecting wipes.', 'Additional recommendations include: Clean your seat, armrest, touchscreen, etc.', 'with a disinfecting wipe once inside an aircraft or other vehicle.', 'Also use a disinfecting wipe to clean key surfaces, doorknobs, remote controls, etc at the hotel or other accommodation where you and your children are staying.', 'Can pregnant women pass coronavirus to unborn children?', 'At this time, there is not enough evidence to determine whether the virus is transmitted from a mother to her baby during pregnancy, or the potential impact this may have on the baby.', 'This is currently being investigated.', 'Pregnant women should continue to follow appropriate precautions to protect themselves from exposure to the virus, and seek medical care early, if experiencing symptoms, such as fever, cough or difficulty breathing.', 'Is it safe for a mother to breastfeed if she is infected with coronavirus?', 'All mothers in affected and at-risk areas who have symptoms of fever, cough or difficulty breathing, should seek medical care early, and follow instructions from a health care provider.', 'Considering the benefits of breastfeeding and the insignificant role of breastmilk in the transmission of other respiratory viruses, the mother can continue breastfeeding, while applying all the necessary precautions.', 'For symptomatic mothers well enough to breastfeed, this includes wearing a mask when near a child (including during feeding), washing hands before and after contact with the child (including feeding), and cleaning/disinfecting contaminated surfaces – as should be done in all cases where anyone with confirmed or suspected COVID-19 interacts with others, including children.', 'If a mother is too ill, she should be encouraged to express milk and give it to the child via a clean cup and/or spoon – all while following the same infection prevention methods.']\n"
     ]
    }
   ],
   "source": [
    "#Tokenization\n",
    "text = corpus\n",
    "sentence_list = nltk.sent_tokenize(text) # A list of sentences\n",
    "print(sentence_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "id": "IWjDcXX7FGA8"
   },
   "outputs": [],
   "source": [
    "# A function to return a random response to a user's greeting\n",
    "def greeting_response(text):\n",
    "  text = text.lower()\n",
    "\n",
    "  #Bots greeting response\n",
    "  bot_greetings = [ 'howdy','hi','hey','hello','hola']\n",
    "  #Users greeting\n",
    "  user_greetings = ['hi','hey','hello','hola', 'greetings','wassup','sup','hey bot','konnichiwa']\n",
    "\n",
    "\n",
    "  for word in text.split():\n",
    "   if word in user_greetings:\n",
    "     return random.choice(bot_greetings)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "Qszgc-r5JUNc"
   },
   "outputs": [],
   "source": [
    "def index_sort(list_var):\n",
    "    length = len(list_var)\n",
    "    list_index = list(range(0,length))\n",
    "\n",
    "    x =list_var\n",
    "    for i in range(length):\n",
    "      for j in range(length):\n",
    "        if x[list_index[i]] > x[list_index[j]]:\n",
    "          #swap\n",
    "          temp = list_index[i]\n",
    "          list_index[i] = list_index[j]\n",
    "          list_index[j] = temp\n",
    "\n",
    "    return list_index \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "5ZRqThffF6Vj"
   },
   "outputs": [],
   "source": [
    "#Create the bot's response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "VujKwWvWIIbw"
   },
   "outputs": [],
   "source": [
    "def bot_response(user_input):\n",
    "  user_input = user_input.lower()\n",
    "  sentence_list.append(user_input)\n",
    "  bot_response=''\n",
    "  cm = CountVectorizer().fit_transform(sentence_list)\n",
    "  similarity_scores = cosine_similarity(cm[-1], cm)\n",
    "  similarity_scores_list = similarity_scores.flatten()\n",
    "  index = index_sort(similarity_scores_list)\n",
    "  index = index[1:]\n",
    "  response_flag = 0\n",
    "\n",
    "  j = 0\n",
    "  for i in range(len(index)):\n",
    "    if similarity_scores_list[index[i]] > 0.0:\n",
    "      bot_response = bot_response+' '+sentence_list[index[i]]\n",
    "      response_flag = 1\n",
    "      j= j+1\n",
    "    if j > 2:\n",
    "      break\n",
    "\n",
    "  if response_flag == 0:\n",
    "    bot_response = bot_response+' '+\"I do not understand your query, please try again.\"\n",
    "\n",
    "  sentence_list.remove(user_input)\n",
    "\n",
    "  return bot_response   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Saving the Model and Pipeline\n",
    "import joblib\n",
    "pipeline_file = open(\"covidbot.pkl\", \"wb\")\n",
    "joblib.dump(bot_response, pipeline_file)\n",
    "pipeline_file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "c88DdUbzOwps",
    "outputId": "e6efdfa6-d283-467e-da45-b4b9ae3cdafd"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "COVID Bot: I am COVID Bot. I will answer your queries about Novel COVID-19. If you want to exit type bye.\n",
      "konnichiwa\n",
      "COVID Bot: hello\n",
      "exit\n",
      "COVID Bot: Had a good time, will chat with you later !\n"
     ]
    }
   ],
   "source": [
    "#Your virtual assistance starts from here:\n",
    "print('COVID Bot: I am COVID Bot. I will answer your queries about Novel COVID-19. If you want to exit type bye.')\n",
    "\n",
    "exit_list = ['exit', 'see you later', 'bye', 'quit', 'break', 'sayonara','stop']\n",
    "while(True):\n",
    "  user_input = input()\n",
    "  if user_input.lower()in exit_list:\n",
    "    print('COVID Bot: Had a good time, will chat with you later !')\n",
    "    break\n",
    "  else:\n",
    "    if greeting_response(user_input) != None:\n",
    "      print('COVID Bot:' +' '+greeting_response(user_input))\n",
    "    else:\n",
    "      print('COVID Bot:' +' '+bot_response(user_input))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "9cDUvFytM1Sr"
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [],
   "name": "chatbot-using-nlp.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
