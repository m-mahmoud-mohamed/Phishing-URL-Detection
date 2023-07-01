## Phishing-URL-Detection

# Introduction:
Phishing is a type of social engineering attack that
pretends to be a trustworthy website in order to persuade users into revealing sensitive information, including login credentials or credit card details. serious consequences from these attacks may include identity theft and financial loss. The need for developing efficient techniques for identifying and countering phishing attacks has grown as the frequency of these attempts rises.
Our proposed approach entails the utilization of various machine learning algorithms to effectively identify phishing URLs. By leveraging the power of machine learning, we aim to develop a robust and accurate system that can distinguish between legitimate URLs and those associated with phishing attacks. Through extensive analysis and training on diverse datasets, our approach aims to enhance the detection capabilities and provide a more reliable defense against phishing threats in the online ecosystem.
our approach has given positive results and shown that it is an effective method for identifying phishing websites. In this project, we used random forest, SVC, and logistic regression algorithms to identify phishing websites.

# Methodology:
Our approach consists of four main steps: data collection, feature extraction, feature selection, model training, and data visualization.


  **Data Collection:**
  
  We used a dataset of both phishing and authentic URL. The dataset consisted of more than 11000 websites, half of which were phishing websites and half were legitimate websites.

  
  **Feature Extraction:**
  
  From the website's URL code, we extracted a number of features, such as the length of the URLs, the length of the path of the links, and the existence of a few terms frequently employed in phishing scams. The most pertinent features for phishing website detection were found using feature selection methods.

  
  **Feature selection:**
  
  In the feature extraction section of our phishing URL detection project, we employed a comprehensive set of feature selection algorithms, including Pearson, Chi-2, Recursive Feature Elimination (RFE), Logistics, Random Forest, and LightGBM. Each of these algorithms was tasked with selecting the top 10 most relevant features from the dataset. By leveraging their unique methodologies and statistical techniques, these algorithms aimed to identify the most discriminative characteristics that differentiate phishing URLs from legitimate ones.
  Once the feature selection process was completed, we performed a voting mechanism to determine the most prominent features. The 10 features chosen by each algorithm were collected, and the frequency of selection for each feature was calculated. Finally, we determined the 13 features with the highest overall frequency of selection across all the feature selection algorithms.
  <img width="760" alt="image" src="https://github.com/m-mahmoud-mohamed/Phishing-URL-Detection/assets/78882792/d4c64769-a441-4727-a83a-3739851c7be7">
  By employing this multi-algorithmic approach, we aimed to enhance the effectiveness and robustness of our feature extraction process, ensuring that the most informative features were identified and utilized for accurate phishing URL detection. This methodology allowed us to harness the strengths of different algorithms and leverage their collective insights to build a more comprehensive and reliable detection system.
  By utilizing these techniques, the goal is to identify the ten most influential features that exhibit strong relationships with the target variable. This data selection phase plays a crucial role in subsequent analyses, as it helps focus on the most informative features, leading to more accurate models and valuable insights.

  
  **Model Training:**
  
  We trained several machine learning algorithms, including logistic regression, support vector classifier, and random forests, using the selected features to classify the websites as either
  phishing or legitimate. The split between training and testing the models was 70:30.

# Results:
Our approach achieved an accuracy of 89% in detecting phishing websites. The random forest model performed the best, with an accuracy of 88%. The precision, recall, and F1- score were also high, indicating that our approach can effectively detect phishing websites. The other two models performed less effectively as the support vector classifier is 79% and the logistic regression was least with an accuracy of 75%.

<img width="571" alt="image" src="https://github.com/m-mahmoud-mohamed/Phishing-URL-Detection/assets/78882792/3ea466f7-c513-41f0-8809-19a05c08c1d2">



