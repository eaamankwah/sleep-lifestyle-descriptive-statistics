#!/usr/bin/env python
# coding: utf-8

# # Transformational AI: Analyzing Ecommerce Large Datasets for Machine Learning
# 
# Welcome to your journey as a data scientist at Transformational AI, where you will play a pivotal role in shaping the future of our company's machine learning models. In this project, you will leverage two Amazon Reviews 2023 datasets, originally sourced from Hugging Face, to perform data transformation, analysis, and visualization. Through this notebook, you will gain hands-on experience with pandas DataFrames and explore powerful data visualization techniques using `seaborn` and `matplotlib`. You will also learn to export your cleaned and processed data into `.csv` and `.parquet` formats, ready for advanced machine learning tasks. Get ready to dive into the world of data science and make impactful contributions to our machine learning team by preparing top-quality datasets for model fine-tuning and customer satisfaction analysis.
# 
# Do not worry if this sounds like a lot right now. Transformational AI makes no mistakes and we hired you for a reason. We will take this one step at a time, and know you have our full support every step of the way. We will be using a lot of advanced language and words, which will add to your Pythonic knowledge and background, while, reinforcing core concepts that you will need to know for your upcoming PCEP exam.
# 
# We know you can do it and we cannot wait to see what you create. Let’s get started!

# # Part 1: Preparing the Environment

# ## Part 1.1: Learn about Jupyter Notebooks & Python Virtual Environments
# 
# When working with Python for a company, organization, or personal project, it's essential to initialize your Python environment properly. Remember from the course the concept of a Python "virtual environment." This isolated environment allows you to write functions, store variables, work with data, and perform many other operations without interfering with other projects or the system Python environment.
# 
# In this step, we will set up and use the Python environment within Jupyter Notebook, which is an interactive computing environment. This will assist us in our tasks at Transformational AI, enabling us to efficiently manage and analyze data, write and test code, and visualize results.
# 
# If you remember from course, Python is a versioned language, and software packages are versioned as well. Let's check out which version of Python is installed thanks to our Jupyter Notebook and also let's check which version of Jupyter Notebook is installed here for us to use as well.
# 
# Run the following commands to check these values:

# In[1]:


# Check which version of Python is installed
get_ipython().system('python --version')

# Check which version of Jupyter Notebook you are using
get_ipython().system('jupyter-notebook --version')


# ## Part 1.2: Set Up the Jupyter Notebook
# 
# To get started, we need to ensure that our Jupyter Notebook environment is equipped with the necessary libraries to run what we need to run. These libraries will help us manage data, create visualizations, and interact with our notebook more effectively.
# 
# For your work in this notebook, you will need the following packages:
# 
# - `datasets`: Providres access to a wide range of datasets, including the Amazon Reviews 2023 dataset we'll be using.
# - `pandas`: A powerful data manipulation and analysis library that makes working with structured data easy with Python.
# - `matplotlib`: A comprehensive library for creating static, animated, and interactive visualizations in Python.
# - `seaborn`: Built on top of matplotlib, seaborn provides a high-level interface for drawing attractive and informative statistical graphics, great for visualizing trends from data.
# - `pyarrow`: A fast and efficient library for reading and writing data in the Apache Arrow format, like Parquet and Feather, to handle large amounts of data efficiently.
# 
# 👉 Do not worry about memorizing these packages this for the PCEP exam. However, as you continue to build upon your Python skills moving forward, these packages will be great tools to have in your toolbox.
# 
# Run a command to install these packages into the Jupyter Notebook envionment:

# In[110]:


#<---- YOUR CODE GOES HERE ---->
#!pip install datasets pandas matplotlib seaborn pyarrow


# In[3]:


get_ipython().system("pip list | grep -E 'datasets|pandas|matplotlib|seaborn|pyarrow'")


# ^ Note: If you see what looks like an error message that looks like this: `ERROR: pip's dependency resolver does not currently take into account all the packages that are installed....` do not worry. As long as you see this line `Successfully installed...` at the end, the packages have been installed successfully. Additionally, you might see the output: `Requirement already satisfied`, which means that the packages are preinstalled as part of the Jupyter Notebook workspace environment, and there's no need to install them again. Both messages are completely normal.

# # Part 2: Download the Reviews Dataset:

# ## Part 2.1: Learn about Working with Big Data
# 
# In this part, we will load the `Electronics` dataset using the Hugging Face datasets library into our Jupyter Notebook.
# 
# ### Working with large datasets:
# 
# NOTE: We are working with a **BIG dataset**, so if we had all the time in the world, we could work through this **22.6 GB** into the notebook. However, we are in a time crunch and don't have time for you to utilize the entire dataset. We need to understand very quickly what products are the best, so let's take a subset of the dataset to use. Do not worry if it appears like the data is going slowly, this is just part of the data science. Consider going to get a cup of your favorite warm beverage ☕️ and coming back when it's done downloading.
# 
# ### Exploring DataFrames:
# 
# To understand how to work with data in Python, `pandas` is a fantastic library that is widely used and very popular. In your work at Transformational AI, you will be using the `pandas` framework and to analyze the data in a `DataFrame`.
# 
# You can think of `DataFrames` as a data structure packet that lets you work with data that could be in different formats or was from many different places, and has then been consolidated into a Pythonic, easy-to-work-with, structure. A `DataFrame` lets us do basic operations like viewing data, checking data types, and basic statistics, all within our Jupyter Notebook. How cool, right? 😎

# ## Part 2.2: Download and visualize the reviews dataset with `pandas`
# 
# - For your first task at Transformational AI, we will be utilizing the `Electronics` dataset in order to help our machine learning engineers better understand what types of products are producing the most optimal customer engagement and attention.
# 
# - While we could guess what products people like, Transformational AI is a data-driven company first and foremost. We will be relying on your to make data-informed decisions about which products are the most valuable for customers. The data you supply to the team will be very important for the training operations of their model outputs, so we will need to work quickly and diligently in order to make sure you can supply the ML team with the most optimal data possible.
# 
# - When you work with software packages in Python, they will often come with a suite of options, or parameters, to tell the underlying core functions what to do. Sometimes, these inputs will be strings, booleans, integers, floats, or other types of data type inputs.
# 
# - First, you will be loading into your Jupyter Notebook an Amazon Reviews dataset from 2023. In order to move quickly, we will only be pulling the first 100 items. After all, we don't have all day and have a very important deadline to meet this week. Speed is of the essence.
# - You will load the data incrementally into a `pandas` DataFrame that will be set with a hard limit of 100 items in a for loop.
# - Additionally, the `load_dataset` module will need edits to input the right parameters, in this case, boolean values for `streaming` and `trust_remote_code`.
#   - You do not need to know what these parameters are doing behind the scenes, but the underlying boolean operators will tell the `datasets` package what to do - a great use of boolean operators here.
# - Afterwards, we will then print the table of outputs as a rich HTML table visualization.
# 
# #### Steps to Complete:
# - [ ] Set the sample_limit to an integer value of 100 so that no more than 100 data items will be collected from the dataset
# - [ ] Create a for loop like you learned about from class so that you increment up to and including 100 data samples
# - [ ] Use boolean operators to set the missing `load_dataset` parameters to `True`.

# In[6]:


from datasets import load_dataset
import pandas as pd

# Load the reviews dataset
reviews_dataset = load_dataset(
    "McAuley-Lab/Amazon-Reviews-2023",
    "raw_review_Electronics",
    split="full",
    streaming=, #<---- YOUR CODE GOES HERE ---->,
    trust_remote_code= #<---- YOUR CODE GOES HERE ---->
)

# Initialize an empty list to collect review samples
reviews = []

# Limit the number of data samples collected
sample_limit =  #<---- YOUR CODE GOES HERE ---->

# Iterate over the reviews dataset and collect samples
for i, review in enumerate(): #<---- YOUR CODE GOES HERE ---->
    if i >= sample_limit: #<---- YOUR CODE GOES HERE ---->
        break
    reviews.append() #<---- YOUR CODE GOES HERE ---->)

# Convert the list of review samples to a pandas DataFrame
reviews_df = pd.DataFrame(reviews)

# Print the dataframe
reviews_df


# ## Let's Reflect...
# ### 💭 Question 1: Describe the data that you see. What are the columns, what data types do you see, and how are the reviews structured?
# Note: By running the following cell, this will create an input field for you to enter your answer and/or code for the questions' defined variable: `QuestionX`. You will see an output of your question by pressing `ENTER` once you are done writing your response in the input field.

# In[ ]:


Question1 = str(input("Write Your Answer in the Box and Press Enter:"))

if len(Question1) > 0:
    print(f"Question answered! You wrote: {Question1}")
else:
    print("Please answer the question")


# ## Part 2.3: Analyze the reviews dataset with `.head()` from `pandas`
# - In the above cell, when we wrote `reviews_df` - we printed the Amazon review data we downloaded as rich HTML outputs. Jupyter notebooks have many great data visualization tools, such as render the DataFrame as a rich HTML table, which is readable and visually appealing as it comes with pagination and the ability to show the first few and last few items in the DataFrame, making it visually interesting and interactive to work with.
# 
# - There will be some times where this is sufficient, especially to get a nice visualzation, but there will be other times where you need to leverage `pandas` a bit more, such as quickly gathering the first few items of the DataFrame with a method called `.head()` which you will do in the subsequent cells.
# 
# - The `.head()` method from `pandas` prints the DataFrame in a plain text format, which can be extremely useful for quickly inspecting the first few rows of the DataFrame without overwhelming the display with lots of data if you have a lot of columns or information to work with.
# 
# Let's try out this new data inspection method!

# In[7]:


print(reviews_df.head())


# ## Let's Reflect...
# ### 💭 Question 2: What do you think of this output above - was this what you expected? Why or why not?
# Note: By running the following cell, this will create an input field for you to enter your answer and/or code for the questions' defined variable: `QuestionX`. You will see an output of your question by pressing `ENTER` once you are done writing your response in the input field.

# In[ ]:


Question2 = str(input("Write Your Answer in the Box and Press Enter:"))

if len(Question2) > 0:
    print(f"Question answered! You wrote: {Question2}")
else:
    print("Please answer the question")


# ## Part 2.4 - Transform the DataFrame to be more visually readable
# 
# As you work with data at Transformational AI, you will see that what we get from another team, department, or company will not be up to our standards. `Pandas` returned the data in 5 output blocks. You will notice that the items 0-4, mean that it's giving us the first 5 items in our dataset. This is what we would expect. However, wouldn't it be easier to see all the data for an item on the same line?
# 
# Let's set some options for how `pandas` will output our dataframe. Remember from the course that you can set values, or options, for various structures. the `pd` `dataframe` is one of those that we can control the outputs for, such as:
# - `max_columns`
# - `width`
# - `max_colwidth`
# - and so on...
# 
# #### Steps to Complete:
# - [ ] Set the `Items_To_Print` value to an integer of `10` so that we only output the first 10 items of the DataFrame, overwriting Pandas' default output.

# In[8]:


import pandas as pd

Items_To_Print = #<---- YOUR CODE GOES HERE ---->

# Adjust display options for better readability
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.width', 1000)        # Set a larger display width
pd.set_option('display.max_colwidth', 50)   # Set max column width for better readability

# Assuming reviews_df is your DataFrame
print(reviews_df.head(10))


# ## Let's Reflect...
# ### 💭 Question 3: Describe what we did to the pandas DataFrame in order to change how the outputs are reflected.
# Note: By running the following cell, this will create an input field for you to enter your answer and/or code for the questions' defined variable: `QuestionX`. You will see an output of your question by pressing `ENTER` once you are done writing your response in the input field.

# In[ ]:


Question3 = str(input("Write Your Answer in the Box and Press Enter:"))

if len(Question3) > 0:
    print(f"Question answered! You wrote: {Question3}")
else:
    print("Please answer the question")


# # Part 3: Download the Reviews Metadata Dataset:
# 
# In this next part, you will be reviewing the metadata associated with reviews. This will give us more topical information about the actual products we want to analyze.

# ## Part 3.1: Download and visualize the reviews metadata dataset with `pandas`
# 
# We will be working with a different dataset, specifically scoped on the metadata around the reviews. This will give us more numeric data about the products the machine learning team at Transformational AI wants to know more about.
# 
# #### Steps to Complete:
# - [ ] Set the metadata_limit to an integer value of 100 so that no more than 100 data items will be collected from the dataset
# - [ ] Create a for loop like you learned about from class so that you increment up to and including 100 data samples
# - [ ] Use boolean operators to set the missing `load_dataset` parameters to `True`.

# In[9]:


from datasets import load_dataset
import pandas as pd

# Load the item metadata dataset
item_metadata_dataset = load_dataset(
    "McAuley-Lab/Amazon-Reviews-2023",
    "raw_meta_Electronics",
    split="full",
    streaming= , #<---- YOUR CODE GOES HERE ---->,
    trust_remote_code= #<---- YOUR CODE GOES HERE ---->
)

# Initialize an empty list to collect item metadata samples
metadata = []

# Limit to 100 samples
metadata_limit =  #<---- YOUR CODE GOES HERE ---->

# Iterate over the metadata dataset and collect samples
 #<---- YOUR CODE GOES HERE ---->
    if i >= metadata_limit: #<---- YOUR CODE GOES HERE ---->
        break
    metadata.append(item) #<---- YOUR CODE GOES HERE ---->)

# Convert the list of item metadata samples to a pandas DataFrame
item_metadata_df = pd.DataFrame(metadata)

# Print the dataframe
item_metadata_df


# ## Let's Reflect...
# ### 💭 Question 4: Compare the Reviews Metadata dataset (the dataset immediately above this cell) and the Reviews dataset that you analyzed earlier. What are the differences between the 2 datasets?
# Note: By running the following cell, this will create an input field for you to enter your answer and/or code for the questions' defined variable: `QuestionX`. You will see an output of your question by pressing `ENTER` once you are done writing your response in the input field.

# In[ ]:


Question4 = str(input("Write Your Answer in the Box and Press Enter:"))

if len(Question4) > 0:
    print(f"Question answered! You wrote: {Question4}")
else:
    print("Please answer the question")


# ## Part 3.2: Analyze the reviews metadata dataset with .head() from pandas
# 
# We will now use the `.head()` method again to analyze the `pandas` dataframe.

# In[10]:


print(item_metadata_df.head(10))


# ^ Did you notice that now when we use the `.head()` method, our `pandas` output preferences were saved? This is the value of the Pythonic environment we are using, because as we set variables or settings declarations, they are preserved throughout the environment when we need to reference them again. This will save you lots of time as you continue your work here at Transformational AI.

# ## Part 3.3: Safeguarding Data Access with Large Datasets
# 
# Now that you are working with DataFrames and large datasets in Python, let's analyze our data a bit before moving on to the next section. Data analysis usually involves reviewing, investigating, or looking up specific information within the larger data context. However, this can lead to errors, especially if the data isn't formatted correctly, if data is missing, or if outputs aren't always consistent. As we work with Python, we will want to ensure our work remains robust and error-free at Transformational AI.
# 
# Let's look at how to search for product prices and discover more about the item_metadata_df data that we imported into our Jupyter Notebook. We will need a function to handle situations where the product information might be missing to manage lookup and indexing errors that can arise.
# 
# #### Steps to Complete:
# - [ ] Review the items with and without a price
# - [ ] Finish the `get_product` lookup function by handling the exception case where the product title or price is not found using try-except blocks
# 

# In[11]:


import pandas as pd

# Ensure the 'price' column is converted to numeric, setting errors='coerce' to handle non-numeric values
item_metadata_df['price'] = pd.to_numeric(item_metadata_df['price'], errors='coerce')

# Identify products with 'None' or non-float prices
none_price_products = item_metadata_df[item_metadata_df['price'].isna()][['title', 'price']]
valid_price_products = item_metadata_df[item_metadata_df['price'].notna()][['title', 'price']]

# Print the list of products with 'None' or non-float prices
print(f"❌ Products with no valid price listed (Total: {len(none_price_products)})")
for i, row in enumerate(none_price_products.itertuples(index=False), start=1):
    print(f"{i}. {row.title} - Price: {row.price}")

# Print the list of products with valid prices
print(f"\n✅ Products with valid price listed (Total: {len(valid_price_products)})")
for i, row in enumerate(valid_price_products.itertuples(index=False), start=1):
    print(f"{i}. {row.title} - Price: {row.price}")


# ### Create a product lookup function with exception handling

# In[12]:


# Function to get the price of a product by its title
def get_product(product_title):
    try:
        # Attempt to find the price of the product
        price = item_metadata_df.loc[item_metadata_df['title'] == product_title, 'price'].values[0]
        if pd.isna(price):
            return "❌ No valid price listed"
        return price
    except IndexError:
        # Handle the case where the product title is not found
        #<---- YOUR CODE GOES HERE ---->
        return "❌ Product not found"


# ### Test the product lookup function (known product title)
# Check a specific item (with a known product title) in the DataFrame with a lookup:

# In[13]:


known_title = "FS-1051 FATSHARK TELEPORTER V3 HEADSET"
print(f"\nPrice of '{known_title}': {get_product(known_title)}")


# ### Test the product lookup function (unknown product title)

# In[14]:


unknown_title = "Smart Phone Tripod Holder (Mobile Version)"
print(f"Price of '{unknown_title}': {get_product(unknown_title)}")


# Above, you can see how we can handle data access errors gracefully. By implementing exception handling in the `get_product` function, you can manage cases where the product title is not found or the price is missing, ensuring your code is robust and reliable.

# # Part 4: Comparing our Datasets Together
# 
# To get a better sense of these two datasets we just downloaded, let's review their columns. This will give us a better sense of the data structures involved, data types, and how we can use the datasets for which purposes.

# ## Part 4.1 Review the columns of the Datasets with `.columns`:
# 
# In order to analyze the datasets quickly, we can leverage our `pandas` DataFrames several ways, such as looking at the `columns` in each dataset.
# 
# #### STEPS TO COMPLETE:
# Place the right variable in the right spot:
# - [ ] `reviews_df.columns`
# - [ ] `item_metadata_df.columns`

# In[15]:


print("Reviews DataFrame columns:", reviews_df.columns) #<---- YOUR CODE GOES HERE ---->)
print("-------------------")
print("Metadata DataFrame columns:", item_metadata_df.columns) #<---- YOUR CODE GOES HERE ---->)


# The above is helpful, but it is a bit messy to read. Let's use our new skills to create a for loop to iterate over the items so that they can be outputted as a list.
# 
# #### STEPS TO COMPLETE:
# - [ ] Update the for loops to output the right information

# In[16]:


print("Reviews DataFrame columns:")
 #<---- YOUR CODE GOES HERE ---->
    print(f"- {column}")

print("-------------------")

print("Metadata DataFrame columns:")
 #<---- YOUR CODE GOES HERE ---->
    print(f"- {column}")


# ## Part 4.2 Review the data types for each dataset with `.dtypes`
# 
# Next, let's analyze what the "data structure" is for each item. If you remember from the course, data structures can be text (strings), number (integer, float, etc.), etc. They are the "types" that data can be used to compare or contrast against.
# 
# For our purposes, we want to get a better sense of the data that we pulled into our environment for the Machine Learning team to later use.

# In[17]:


# Print column names and their data types using .dtypes
print("Reviews DataFrame columns and data types:")
print(reviews_df.dtypes)

print("-------------------")

print("Metadata DataFrame columns and data types:")
print(item_metadata_df.dtypes)


# The above is helpful, but let's use a for loop to iterate over the items so that they can be outputted as a list:

# In[18]:


# Print column names and their data types
print("Reviews DataFrame columns and data types:")
for column in reviews_df.columns:
    print(f"- {column}: {reviews_df[column].dtype}")

print("-------------------")

print("Metadata DataFrame columns and data types:")
for column in item_metadata_df.columns:
    print(f"- {column}: {item_metadata_df[column].dtype}")


# ## Part 4.3 Create a concise summary of a DataFrame with `.info()`
# 
# While you were analyzing your data, your manager messages you asking for a quick summary of the breakdown between the summaries in the next 15 minutes. Scrambling to what to do, you remember that you can use the `.info()` method from `pandas` to get your manager exactly what they need.
# 
# - If you remember from class, a `method` in Python is a function that is associated with an object. `.info()` is method of the pandas DataFrame class where when you call `something_df.info()`, you are invoking the "info" method on the `something_df` object, which is an instance of a DataFrame.
# - Also, if you recall from class, the act of calling a method (like `.info()`) on an object (like `something_df`) is known as method `invocation`, which is fundamental to how Python works as an object-oriented programming language.
# 
# #### STEPS TO COMPLETE:
# - [ ] Print the info for the `reviews_df` DataFrame
# - [ ] Print the info for the `item_metadata_df` DataFrame

# In[20]:


# Print DataFrame info which includes data types
print("Reviews DataFrame info:")
reviews_df.info() #<---- YOUR CODE GOES HERE ---->

print("-------------------")

print("Metadata DataFrame info:")
 #<---- YOUR CODE GOES HERE ---->


# ## ^ Phew! 😅 That was a close call.
# But fortunately for us, `pandas` comes with a lot of out of the box utilities for data analysis and data visualization that we might need to tweak or fine-tune to our usecases but without too much headache. Let's get back to our work at hand.
# 
# Great work!!

# ## Let's Reflect...
# ### 💭 Question 5: Which data analysis method you find to be the most insightful or helpful?
# Note: By running the following cell, this will create an input field for you to enter your answer and/or code for the questions' defined variable: `QuestionX`. You will see an output of your question by pressing `ENTER` once you are done writing your response in the input field.

# In[ ]:


Question5 = str(input("Write Your Answer in the Box and Press Enter:"))

if len(Question5) > 0:
    print(f"Question answered! You wrote: {Question5}")
else:
    print("Please answer the question")


# # Part 5: Preparing the Data for the Machine Learning Team
# 
# Now that we are comfortable with our datasets and have a good sense of what we can leverage, the Machine Learning team has just informed you that they need to know what the top products are to train their advanced machine learning model on.
# 
# You will be further cleaning and transforming the data so that you can create an informed, data-driven decision about what products are most important to the team.
# 
# So where would we start? Let's assume that we need a threshold value in order to separate what makes a good product from a great product. If you remember from earlier, on the metadata
# 
# - `title`: we need to know the product
# -	`average_rating`: we need to know if the product is above the treshold we set (4.5 or above)
# - `price`: we need a real monetary price value. Notice how sometimes it could be NONE. We need something that is number with a decimal. (0.01 and above)
# 

# ## Part 5.1: Clean the Data for the Requested Parameters
# 
# We will create a new DataFrame called `top_products_df` with these parameters:
# - has a title
# - the average rating is greater than or equal to 4.5
# - there is a value for the price
# 
# #### STEPS TO COMPLETE:
# - [ ] Specify the 3 columns we want in the new dataframe `item_metadata_cleaned_df`
# - [ ] Set the `average_rating_filter` variable to the correct float data type that is sought after in the instructions above

# In[21]:


# Select relevant columns
item_metadata_cleaned_df = item_metadata_df[['title', 'average_rating', 'price']]
average_rating_filter  #<---- YOUR CODE GOES HERE ---->

# Convert the price column to numeric, setting errors='coerce' to handle non-numeric values
item_metadata_cleaned_df.loc[:, 'price'] = pd.to_numeric(item_metadata_cleaned_df['price'], errors='coerce')

# Filter to get only products with average rating set to the filter, valid price, and non-null title
top_products_df = item_metadata_cleaned_df[
    (item_metadata_cleaned_df['average_rating'] >= average_rating_filter) &
    (item_metadata_cleaned_df['price'].notna()) &
    (item_metadata_cleaned_df['title'].notna())
]

# Print the new cleaned DataFrame
top_products_df


# ## Part 5.2: Analyze the Data Using pandas
# 
# Let's find out how many products are in this new cleaned dataset.

# In[22]:


# Review the items of the original dataframe
num_items_original = item_metadata_df.shape[0]
print(f"Number of items in the original DataFrame: {num_items_original}")

# Review the new items in cleaned dataframe
num_items_cleaned = top_products_df.shape[0]
print(f"Number of items in the cleaned DataFrame: {num_items_cleaned}")


# ## Part 5.3: Calculate the Percentage of Cleaned Data
# 
# You should see that the number of items in the cleaned DataFrame is much smaller than the number of items in the original DataFrame. Let's calculate the percentage of items in the cleaned DataFrame relative to the original DataFrame.
# 
# #### STEPS TO COMPLETE:
# - [ ] Complete the function `calculate_percentage` to perform this calculation. Use your knowledge from the course to write a part-of-whole division equation.
# - [ ] Ensure to use the `return` keyword so that your `calculate_percentage` function returns the result.

# In[23]:


part = float(input("Enter the number of items in the cleaned DataFrame: "))
whole = float(input("Enter the number of items in the original DataFrame: "))

# Function to calculate percentage
def calculate_percentage(part, whole):
    if whole == 0:
        raise ValueError("The whole value cannot be zero.")

    # Calculate the percentage
    percentage =  #<---- YOUR CODE GOES HERE ---->
    return  #<---- YOUR CODE GOES HERE ---->

# Calculate and print the percentage
try:
    result = calculate_percentage(part, whole)
    print(f"{part} is {result:.2f}% of {whole}")
except ValueError as e:
    print(e)


# ## Part 5.4: Package the Dataset up for Analysis (.csv)
# 
# In order to save our new dataset, let's package it up into a `.csv` file so that your team at Transformational AI can analyze the outputs you found.

# In[24]:


# Save the DataFrame as a CSV file
top_products_df.to_csv('top_products.csv', index=False)

# Verify that the file is saved
get_ipython().system('ls -lh top_products.csv')


# ## Part 5.5: Package the Dataset up for Analysis (.parquet)
# 
# You might find that various team members need data saved in particular ways. For example, dependending on how data is coordinated or analyzed, `.csv` might not cut it. There is a movement to move towards size-saving strategies, which can mean saving data in other formats.
# 
# Luckily, your team member at Transformational AI gave you a heads up about the team's love for the `.parquet` format. In order to impress your team and new manager, you have just enough time to transform your data outputs into this format.

# In[25]:


# Save the DataFrame as a Parquet file
top_products_df.to_parquet('top_products.parquet', index=False)

# Verify that the file is saved
get_ipython().system('ls -lh top_products.parquet')


# Really great work! 🥳 You'll now be able to send both files along to the teams, one for easy visualization (`.csv`), and one for easy data use (`.parquet`)

# ## Part 5.6: Collect the Top Rated Product Titles
# 
# When working with large datasets like the reviews datasets we are using, we might need to handle the data with lists and exceptions. These are fundamental Python skills that are important to know and have in your toolbox.
# 
# - Lists are a type of data structure that let's us store multiple items as a single variable
# - To work with them, we will use the `append` method to collect the data and "add" it to a single variable to reference it in our work.
# - In this case, we will be pulling out the titles from our `top_products_df` DataFrame and storing those in our list, which we will create and name `top_rated_titles`.
# 
# #### STEPS TO COMPLETE:
# - [ ] Create an empty array called `top_rated_titles` which will be our list.
# - [ ] Create a for loop to iterate over the `top_products_df` DataFrame and then use the `.append` method for the titles to add them to the `top_rated_titles` list
# - [ ] Print the results of the `top_rated_titles` list

# In[26]:


# Initialize an empty list to collect top-rated product titles
top_rated_titles = []
#<---- YOUR CODE GOES HERE ---->

# Create a for loop to iterate over the highly_rated_products_df DataFrame
# Use the `append` method for the titles to add them to the `top_rated_titles` list
#<---- YOUR CODE GOES HERE ---->
for title in top_products_df['title']:
    top_rated_titles.append(title)

# Print the list of top-rated product titles
print("List of Top-Rated Product Titles:")
#<---- YOUR CODE GOES HERE ---->
print(top_rated_titles)


# ## Part 5.7: Transforming our List Data
# You might notice that when we print the values, it becomes a very long string. This is because lists become a comma separated long string, enclosed in square brackets. This is a default behavior of Python, which can be efficient to work with in certain cases. However, let's make the list a bit more human readable.
# 
# Something we can do is iterate through the list and print each item in the list separately and add numbers or bullet points to each element.
# 
# Run the following cell to do this:

# In[27]:


for i, title in enumerate(top_rated_titles, start=1):
    print(f"{i}. {title}")


# ^ This looks much better and easier to read. Great work!

# # Part 6: Visualize the Data for the Business Team
# 
# To visualize our data, we will be using a Histogram. Histograms are a type of graph that coordinates groups of data points into user-specified ranges (bins). Each bar in a histogram represents the frequency (the count) of data points that fall within each range.
# 
# We will also be using a Scatterplot graph, which will show the exact points that the histogram creates groupings of.

# ## Part 6.1: Map the Distribution of Prices for Highly Rated Products as a Histogram Chart
# In this graph, we will want to see if there is a trend for price and ratings, specifically to visualize the distribution of prices for highly rated products (those with an average rating of 4.5 or higher).
# 
# #### STEPS TO COMPLETE:
# - [ ] Use the `top_products_df` dataframe for the histogram graph
# - [ ] Use the `price` column from the `top_products_df`
# - [ ] Use a boolean operator to set the missing `sns.histplot` parameter `kde`  to `True`.
# 

# In[28]:


import seaborn as sns
import matplotlib.pyplot as plt

# Distribution of Prices
plt.figure(figsize=(10, 6))
sns.histplot(
    top_products_df['price'],
    bins=30,
    kde= #<---- YOUR CODE GOES HERE ---->
)
plt.title('Distribution of Prices for Highly Rated Products')
plt.xlabel('Price')
plt.ylabel('Frequency of Rating')
plt.show()


# ## Let's Reflect...
# ### 💭 Question 6: What trend (if any) do you notice with price and frequency?
# Note: By running the following cell, this will create an input field for you to enter your answer and/or code for the questions' defined variable: `QuestionX`. You will see an output of your question by pressing `ENTER` once you are done writing your response in the input field.

# In[ ]:


Question6 = str(input("Write Your Answer in the Box and Press Enter:"))

if len(Question6) > 0:
    print(f"Question answered! You wrote: {Question6}")
else:
    print("Please answer the question")


# ## Part 6.2: Map the Distribution of Prices for Highly Rated Products as a Scatterplot Graph
# In this graph, we will want to see if there is a trend for price and ratings, specifically to visualize the distribution of prices for highly rated products (those with an average rating of 4.5 or higher) as a scatterplot, rather than a histogram
# 
# #### STEPS TO COMPLETE:
# - [ ] Use the `top_products_df` dataframe for the scatterplot graph
# - [ ] Plot you graph with the `price` for the x axis and `average_rating` on the y axis

# In[29]:


# Average Rating vs. Price
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=top_products_df, 
    x='price', 
    y='average_rating'
)
plt.title('Average Rating vs. Price')
plt.xlabel('Price')
plt.ylabel('Average Rating')
plt.show()


# ## Let's Reflect...
# ### 💭 Question 7: What trend (if any) do you notice with price and rating?
# Note: By running the following cell, this will create an input field for you to enter your answer and/or code for the questions' defined variable: `QuestionX`. You will see an output of your question by pressing `ENTER` once you are done writing your response in the input field.

# In[ ]:


Question7 = str(input("Write Your Answer in the Box and Press Enter:"))

if len(Question7) > 0:
    print(f"Question answered! You wrote: {Question7}")
else:
    print("Please answer the question")


# ## Part 6.3: Display the Distribution of Ratings and Price Together
# 
# The "frequency" in this context of a histogram or distribution plot refers to the number of times a particular value or range of values appears in the dataset. In our case, we want to know how often the ratings are coming up related to the price.
# 
# For business-facing teams, showing data a couple different ways can be quite helpful, so we will want to visualize these 2 graphs together for maximum impact.

# In[30]:


# Create a Dashboard Layout
plt.figure(figsize=(15, 10))

# Subplot 1: Distribution of Prices
plt.subplot(2, 2, 1)
sns.histplot(top_products_df['price'], bins=30, kde=True)
plt.title('Distribution of Prices for Highly Rated Products')
plt.xlabel('Price')
plt.ylabel('Frequency of Rating')

# Subplot 2: Average Rating vs. Price
plt.subplot(2, 2, 2)
sns.scatterplot(data=top_products_df, x='price', y='average_rating')
plt.title('Average Rating vs. Price')
plt.xlabel('Price')
plt.ylabel('Average Rating')

# Feel free to add other visualizations as you like

# Show the Dashboard
plt.tight_layout()
plt.show()


# ## 6.4: Narrow Down on the Handful of Products that Will be Most Meaningful
# 
# To get a better sense of what products the teams will specifically want to double down on, let's use these graphs to create even better outputs.
# 
# #### STEPS TO COMPLETE:
# - [ ] Specify a cutoff threshold for the results as float data type `4.7`

# In[31]:


# Filter the DataFrame to include only products with an average rating of 4.7 or higher
average_rating_cutoff =  #<---- YOUR CODE GOES HERE ---->
highly_rated_products_df = top_products_df[top_products_df['average_rating'] >= average_rating_cutoff]

# Display the filtered DataFrame
print(highly_rated_products_df)


#  Count the number of items in the newly cleaned dataset

# In[32]:


# Review the new items in cleaned DataFrame
highly_rated_num_items = highly_rated_products_df.shape[0]
print(f"Number of items in the highly rated DataFrame: {highly_rated_num_items}")


# Calculate the percentage of the newly cleaned items with the function you wrote earlier:

# In[33]:


part = float(input("Enter the number of items in the highly rated DataFrame: "))
whole = float(input("Enter the number of items in the original top products DataFrame: "))


# Calculate and print the percentage
try:
    result = calculate_percentage(part, whole)
    print(f"{part} is {result:.2f}% of {whole}")
except ValueError as e:
    print(e)


# Plot the new Histogram distribution with your highly rated DataFrame:

# In[34]:


plt.figure(figsize=(10, 6))
sns.histplot(highly_rated_products_df['price'], bins=30, kde=True)
plt.title('Distribution of Prices for Products with Rating 4.7 or Higher')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()


# Plot the new Scatterplot graph with your new highly rated DataFrame:

# In[35]:


plt.figure(figsize=(10, 6))
sns.scatterplot(data=highly_rated_products_df, x='price', y='average_rating')
plt.title('Average Rating vs. Price for Products with Rating 4.7 or Higher')
plt.xlabel('Price')
plt.ylabel('Average Rating')
plt.show()


# ## 6.5: Create a Dashboard of Your New Findings
# The next step will be to create a dashboard for these new results so that you can share this with the Machine Learning, Business, and Executive teams. This section will involve filtering, sorting, and visualizing data, which are key skills covered in the PCEP syllabus.
# 
# To accomplish this, we'll:
# - Filter the DataFrame: We'll filter the DataFrame to include only products with an average rating of `4.7` or higher.
# - Sort the DataFrame: We'll use the `.sort_values` method to sort the DataFrame by average rating in descending order.
# - Display the DataFrame: We'll display the sorted DataFrame as a table.
# - Create a Scatterplot: We'll create a scatterplot to visualize the relationship between price and average rating for the highly rated products.
# 
# #### STEPS TO COMPLETE:
# - [ ] Set the `highly_rated_products_df_cutoff` with the desired float threshold value
# - [ ] Update the `highly_rated_products_df` to use the `.sort_values` method like you learned in class.
# - [ ] Fill in the code to display the new sorted DataFrame
# - [ ] Complete the code to create a scatterplot using Seaborn.

# In[36]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

# Filter the DataFrame to include only products with an average rating of 4.7 or higher
highly_rated_products_df_cutoff =  #<---- YOUR CODE GOES HERE ---->
highly_rated_products_df = top_products_df[top_products_df['average_rating'] >= highly_rated_products_df_cutoff]

# Sort the DataFrame by average_rating in descending order
highly_rated_products_df = highly_rated_products_df.sort_values(by='average_rating', ascending=False)

# Display the sorted DataFrame as a table
print("Table of Highly Rated Products (Rating 4.7 or Higher, Sorted by Rating):")
display(highly_rated_products_df)

# Create the scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=highly_rated_products_df, x='price', y='average_rating')
plt.title('Average Rating vs. Price for Products with Rating 4.7 or Higher')
plt.xlabel('Price')
plt.ylabel('Average Rating')
plt.show()


# #### Amazing job!! You did it! 🥳 🎉

# # 🎁 Wrap Up
# 
# Congratulations, you completed everything that the Machine Learning Team, the Business Team, and the Executive Team at Transformational AI need to get started. You completed this in record time and your manager is excited to offer you a promotion to the Data Science team thanks to all of your hard work! 🥇
# 
# To wrap up your excellent work, let's output all of your responses to the questions earlier into a `.txt` file. The code is already written for you, but let's look at what is happening:
# - We create an `array` of questions to group all of your data inputs together
# - We create a file name as a string called `output_file` where your responses will be written to.
# - We write a for loop to iterate over each question, which lives inside of a with statement so that we can write each question and response as a line in the text file
# - We use the `print` command to let us know when the file has been created and stored in our notebook.

# ### 💭 Add your name: Write your first and last name here
# Note: By running the following cell, this will create an input field for you to enter your answer and/or code for the questions' defined variable: `Name`. You will see an output of your question by pressing `ENTER` once you are done writing your response in the input field.

# In[ ]:


Name = str(input("Write Your Answer in the Box and Press Enter:"))

if len(Name) > 0:
    print(f"You added your name: {Name}")
else:
    print("Please answer the question")


# In[ ]:


# Collect all the questions into a list
questions = [Question1, Question2, Question3, Question4, Question5, Question6, Question7]

# Define the file name where your answers will be saved to
output_file = 'user_inputs.txt'

# Write the project details and questions to the output file
with open(output_file, 'w') as file:
    # Write the project title and your name
    file.write("Transformational AI: Analyzing Ecommerce Large Datasets for Machine Learning\n")
    file.write(f"Completed by: {Name}\n")
    file.write("—————————————-\n\n")

    # Write each question and its response on subsequent line
    for i, question in enumerate(questions, start=1):
        file.write(f"Question {i}: {question}\n")

print(f"All questions have been written to {output_file}")


# ## Extended Analysis

# ### Product Clustering Analysis
# 
# **Simple K-Means Clustering**

# In[111]:


#!pip install scikit-learn


# In[40]:


# load libraries for clustering analysis
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# In[41]:


# Prepare data for clustering
clustering_data = top_products_df[['price', 'average_rating']].copy()

# Handle any remaining NaN values
clustering_data = clustering_data.dropna()


# In[42]:


# Standardize the features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(clustering_data)


# In[43]:


# Perform K-Means clustering with 3 clusters
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
clusters = kmeans.fit_predict(scaled_data)

# Add cluster labels to the dataframe
clustering_data['cluster'] = clusters


# In[44]:


# Merge clusters back to original dataframe
top_products_df_clustered = top_products_df.copy()
top_products_df_clustered = top_products_df_clustered.loc[clustering_data.index]
top_products_df_clustered['cluster'] = clusters

print("\n" + "=" * 80)
print("K-MEANS CLUSTERING RESULTS")
print("=" * 80)


# In[45]:


# Analyze each cluster
for cluster_id in range(n_clusters):
    cluster_products = top_products_df_clustered[top_products_df_clustered['cluster'] == cluster_id]
    
    print(f"\nCluster {cluster_id + 1}:")
    print(f"  - Number of products: {len(cluster_products)}")
    print(f"  - Average price: ${cluster_products['price'].mean():.2f}")
    print(f"  - Average rating: {cluster_products['average_rating'].mean():.2f}")
    print(f"  - Price range: ${cluster_products['price'].min():.2f} - ${cluster_products['price'].max():.2f}")
    print(f"  - Rating range: {cluster_products['average_rating'].min():.2f} - {cluster_products['average_rating'].max():.2f}")
    
    # Interpret the cluster
    avg_price = cluster_products['price'].mean()
    avg_rating = cluster_products['average_rating'].mean()
    
    if avg_price < clustering_data['price'].median() and avg_rating >= 4.6:
        interpretation = "Budget-Friendly High Quality"
    elif avg_price >= clustering_data['price'].median() and avg_rating >= 4.6:
        interpretation = "Premium High Quality"
    else:
        interpretation = "Standard Products"
    
    print(f"  - Cluster Interpretation: {interpretation}")


# ## Visualize Clusters

# In[46]:


# Create a comprehensive visualization of the clusters.

plt.figure(figsize=(14, 10))

# Subplot 1: Scatter plot with clusters
plt.subplot(2, 2, 1)
scatter = plt.scatter(
    top_products_df_clustered['price'], 
    top_products_df_clustered['average_rating'],
    c=top_products_df_clustered['cluster'],
    cmap='viridis',
    s=100,
    alpha=0.6,
    edgecolors='black'
)
plt.colorbar(scatter, label='Cluster')
plt.xlabel('Price ($)')
plt.ylabel('Average Rating')
plt.title('Product Clusters: Price vs Rating')
plt.grid(True, alpha=0.3)


# In[48]:


# Subplot 2: Cluster size distribution
plt.subplot(2, 2, 2)
cluster_counts = top_products_df_clustered['cluster'].value_counts().sort_index()
bars = plt.bar(range(n_clusters), cluster_counts.values, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.xlabel('Cluster')
plt.ylabel('Number of Products')
plt.title('Products per Cluster')
plt.xticks(range(n_clusters), [f'Cluster {i+1}' for i in range(n_clusters)])

# Add value labels on bars
for i, (bar, count) in enumerate(zip(bars, cluster_counts.values)):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
             str(count), ha='center', va='bottom', fontweight='bold')


# In[49]:


# Subplot 3: Price distribution by cluster
plt.subplot(2, 2, 3)
for cluster_id in range(n_clusters):
    cluster_data = top_products_df_clustered[top_products_df_clustered['cluster'] == cluster_id]['price']
    plt.hist(cluster_data, alpha=0.5, label=f'Cluster {cluster_id + 1}', bins=15)
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.title('Price Distribution by Cluster')
plt.legend()
plt.grid(True, alpha=0.3)


# In[50]:


# Subplot 4: Rating distribution by cluster
plt.subplot(2, 2, 4)
cluster_ratings = [
    top_products_df_clustered[top_products_df_clustered['cluster'] == i]['average_rating'].values 
    for i in range(n_clusters)
]
plt.boxplot(cluster_ratings, labels=[f'Cluster {i+1}' for i in range(n_clusters)])
plt.ylabel('Average Rating')
plt.title('Rating Distribution by Cluster')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('product_clustering_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ Clustering visualization saved as 'product_clustering_analysis.png'")


# ## Generate Executive Summary Statistics

# In[51]:


# Calculate comprehensive statistics
summary_stats = {
    'Total Products Analyzed': len(top_products_df),
    'Average Price': f"${top_products_df['price'].mean():.2f}",
    'Median Price': f"${top_products_df['price'].median():.2f}",
    'Price Std Dev': f"${top_products_df['price'].std():.2f}",
    'Average Rating': f"{top_products_df['average_rating'].mean():.3f}",
    'Median Rating': f"{top_products_df['average_rating'].median():.3f}",
    'Products >=4.8 Rating': len(top_products_df[top_products_df['average_rating'] >= 4.8]),
    'Products <$25': len(top_products_df[top_products_df['price'] < 25]),
    'Budget High-Quality': len(top_products_df[(top_products_df['price'] < 25) & (top_products_df['average_rating'] >= 4.7)]),
    'Number of Clusters': n_clusters
}

print("\n" + "=" * 80)
print("EXECUTIVE SUMMARY STATISTICS")
print("=" * 80)

for key, value in summary_stats.items():
    print(f"{key:.<40} {value}")

# Create a summary DataFrame for export
summary_df = pd.DataFrame([summary_stats])
summary_df.to_csv('executive_summary.csv', index=False)

print("\n✅ Executive summary saved as 'executive_summary.csv'")


# ## Custom Visualizations

# In[54]:


import numpy as np

# Define number of products
n_products = 100 

# Product titles and categories
product_categories = [
    'All Electronics', 'Computers', 'AMAZON FASHION', 'Cell Phones & Accessories',
    'Sports & Outdoors', 'Industrial & Scientific', 'Camera & Photo'
]

# Common product types 
product_prefixes = [
    'Compatible', 'Wireless', 'USB', 'HD', 'Pro', 'Portable', 
    'Smart', 'Digital', 'Premium', 'Universal'
]

product_items = [
    'Headset', 'Cable', 'Band', 'Case', 'Cover', 'Adapter', 'Charger',
    'Mount', 'Screen Protector', 'Lens', 'Backpack', 'USB Drive', 
    'Hard Drive', 'Microphone', 'Speaker', 'Controller'
]

# Generate realistic product titles based on dataset
titles = [
    f"{np.random.choice(product_prefixes)} {np.random.choice(product_items)} "
    f"for {np.random.choice(['iPhone', 'Samsung', 'MacBook', 'iPad', 'Android', 'Gaming Console'])}"
    for i in range(n_products)
]

# Generate price and rating data based on dataset
# From the data: ratings are 4.5-5.0 (filtered for top products)
# Prices range from ~$9.99 to ~$109.99, with many clustering at lower end
base_ratings = np.random.uniform(4.5, 5.0, n_products)

# Real dataset shows: most prices are low ($9.99-$25), fewer high prices
# Using combination of distributions to match this pattern
low_prices = np.random.uniform(9.99, 29.99, int(n_products * 0.7))
mid_prices = np.random.uniform(30.00, 69.99, int(n_products * 0.2))
high_prices = np.random.uniform(70.00, 149.99, int(n_products * 0.1))

prices = np.concatenate([low_prices, mid_prices, high_prices])
np.random.shuffle(prices)

# Ensure we have exactly n_products
prices = prices[:n_products]

# Round prices to 2 decimal places like real data
prices = np.round(prices, 2)

# Note: In actual dataset, there's NO strong correlation between price and rating
# High ratings exist across all price ranges


# In[55]:


# Add some correlation
ratings = base_ratings + (prices / 100) * 0.1 + np.random.normal(0, 0.05, n_products)
ratings = np.clip(ratings, 4.5, 5.0)

# Create DataFrame
top_products_df = pd.DataFrame({
    'title': titles,
    'price': prices,
    'average_rating': ratings,
    'review_count': np.random.randint(10, 1000, n_products),
    'category': [np.random.choice(product_categories) for _ in range(n_products)]
})

# Add derived metrics
top_products_df['value_score'] = top_products_df['average_rating'] / (top_products_df['price'] + 1)
top_products_df['popularity_score'] = top_products_df['review_count'] * top_products_df['average_rating']


# In[56]:


# Perform clustering
scaler = StandardScaler()
scaled_features = scaler.fit_transform(top_products_df[['price', 'average_rating']])
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
top_products_df['cluster'] = kmeans.fit_predict(scaled_features)

print(f"\n✅ Loaded {len(top_products_df)} products for analysis")
print(f"📊 Price range: ${top_products_df['price'].min():.2f} - ${top_products_df['price'].max():.2f}")
print(f"⭐ Rating range: {top_products_df['average_rating'].min():.2f} - {top_products_df['average_rating'].max():.2f}")


# In[57]:


# Visualization 1: Comprehensive Box Plot Analysis

print("\n" + "=" * 80)
print("VISUALIZATION 1: BOX PLOT ANALYSIS")
print("=" * 80)

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Box Plot Analysis: Distribution Insights Across Multiple Dimensions', 
             fontsize=16, fontweight='bold', y=1.00)


# In[63]:


# 1. Price Distribution by Cluster
ax1 = axes[0, 0]
cluster_data = [top_products_df[top_products_df['cluster'] == i]['price'].values 
                for i in range(3)]
bp1 = ax1.boxplot(cluster_data, tick_labels=[f'Cluster {i+1}' for i in range(3)],
                   patch_artist=True, notch=True, showmeans=True)
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
for patch, color in zip(bp1['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax1.set_ylabel('Price ($)', fontsize=10, fontweight='bold')
ax1.set_xlabel('Cluster', fontsize=10, fontweight='bold')
ax1.set_title('Price Distribution by Cluster', fontsize=11, fontweight='bold')
ax1.grid(True, alpha=0.3)

# Add statistical annotations
for i, data in enumerate(cluster_data):
    median = np.median(data)
    ax1.text(i+1, median, f'Med: ${median:.0f}', 
             ha='center', va='bottom', fontsize=8, fontweight='bold')


# In[62]:


# Rating Distribution by Cluster
ax2 = axes[0, 1]
rating_data = [top_products_df[top_products_df['cluster'] == i]['average_rating'].values 
               for i in range(3)]
bp2 = ax2.boxplot(rating_data, tick_labels=[f'Cluster {i+1}' for i in range(3)],
                   patch_artist=True, notch=True, showmeans=True)
for patch, color in zip(bp2['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax2.set_ylabel('Average Rating', fontsize=10, fontweight='bold')
ax2.set_xlabel('Cluster', fontsize=10, fontweight='bold')
ax2.set_title('Rating Distribution by Cluster', fontsize=11, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.set_ylim([4.4, 5.1])


# In[61]:


# Price Distribution by Category
ax3 = axes[0, 2]
categories = top_products_df['category'].unique()
category_price_data = [top_products_df[top_products_df['category'] == cat]['price'].values 
                       for cat in categories]
bp3 = ax3.boxplot(category_price_data, tick_labels=categories,
                   patch_artist=True, notch=True, showmeans=True)
category_colors = plt.cm.Set3(np.linspace(0, 1, len(categories)))
for patch, color in zip(bp3['boxes'], category_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax3.set_ylabel('Price ($)', fontsize=10, fontweight='bold')
ax3.set_xlabel('Category', fontsize=10, fontweight='bold')
ax3.set_title('Price Distribution by Product Category', fontsize=11, fontweight='bold')
ax3.tick_params(axis='x', rotation=45)
ax3.grid(True, alpha=0.3)


# In[64]:


# Value Score Distribution by Cluster
ax4 = axes[1, 0]
value_data = [top_products_df[top_products_df['cluster'] == i]['value_score'].values 
              for i in range(3)]
bp4 = ax4.boxplot(value_data, tick_labels=[f'Cluster {i+1}' for i in range(3)],
                   patch_artist=True, notch=True, showmeans=True)
for patch, color in zip(bp4['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax4.set_ylabel('Value Score (Rating/Price)', fontsize=10, fontweight='bold')
ax4.set_xlabel('Cluster', fontsize=10, fontweight='bold')
ax4.set_title('Value Score Distribution by Cluster', fontsize=11, fontweight='bold')
ax4.grid(True, alpha=0.3)


# In[65]:


# Review Count Distribution (log scale)
ax5 = axes[1, 1]
review_data = [top_products_df[top_products_df['cluster'] == i]['review_count'].values 
               for i in range(3)]
bp5 = ax5.boxplot(review_data, tick_labels=[f'Cluster {i+1}' for i in range(3)],
                   patch_artist=True, notch=True, showmeans=True)
for patch, color in zip(bp5['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax5.set_ylabel('Review Count (log scale)', fontsize=10, fontweight='bold')
ax5.set_xlabel('Cluster', fontsize=10, fontweight='bold')
ax5.set_title('Customer Engagement by Cluster', fontsize=11, fontweight='bold')
ax5.set_yscale('log')
ax5.grid(True, alpha=0.3)


# In[67]:


# Popularity Score Distribution
ax6 = axes[1, 2]
pop_data = [top_products_df[top_products_df['cluster'] == i]['popularity_score'].values 
            for i in range(3)]
bp6 = ax6.boxplot(pop_data, tick_labels=[f'Cluster {i+1}' for i in range(3)],
                   patch_artist=True, notch=True, showmeans=True)
for patch, color in zip(bp6['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax6.set_ylabel('Popularity Score', fontsize=10, fontweight='bold')
ax6.set_xlabel('Cluster', fontsize=10, fontweight='bold')
ax6.set_title('Overall Popularity by Cluster', fontsize=11, fontweight='bold')
ax6.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('boxplot_analysis.png', dpi=300, bbox_inches='tight')
plt.show()


# ## REAL-WORLD BUSINESS USE CASE
# 
# ### Dynamic Pricing Optimization

# In[68]:


# Analyze price elasticity by cluster
pricing_analysis = {}

for cluster_id in range(3):
    cluster_data = top_products_df[top_products_df['cluster'] == cluster_id]
    
    # Calculate price statistics
    price_stats = {
        'avg_price': cluster_data['price'].mean(),
        'median_price': cluster_data['price'].median(),
        'std_price': cluster_data['price'].std(),
        'avg_rating': cluster_data['average_rating'].mean(),
        'avg_reviews': cluster_data['review_count'].mean(),
        'value_score': cluster_data['value_score'].mean()
    }
    
    # Calculate price tiers within cluster
    q1 = cluster_data['price'].quantile(0.25)
    q2 = cluster_data['price'].quantile(0.50)
    q3 = cluster_data['price'].quantile(0.75)
    
    pricing_analysis[cluster_id] = {
        'stats': price_stats,
        'quartiles': {'Q1': q1, 'Q2': q2, 'Q3': q3},
        'products': len(cluster_data)
    }


# In[69]:


print("\n📊 PRICING INSIGHTS BY CLUSTER:\n")
for cluster_id, analysis in pricing_analysis.items():
    print(f"CLUSTER {cluster_id + 1}:")
    print(f"  Products: {analysis['products']}")
    print(f"  Average Price: ${analysis['stats']['avg_price']:.2f}")
    print(f"  Price Range: ${analysis['quartiles']['Q1']:.2f} - ${analysis['quartiles']['Q3']:.2f}")
    print(f"  Average Rating: {analysis['stats']['avg_rating']:.3f}")
    print(f"  Value Score: {analysis['stats']['value_score']:.4f}")
    
    # Pricing recommendation
    if analysis['stats']['avg_rating'] >= 4.7 and analysis['stats']['avg_price'] < 50:
        print(f"  💡 RECOMMENDATION: Premium pricing opportunity (+15-20%)")
        recommended_price = analysis['stats']['avg_price'] * 1.175
        print(f"     → Suggested price: ${recommended_price:.2f}")
    elif analysis['stats']['avg_rating'] < 4.6:
        print(f"  💡 RECOMMENDATION: Competitive pricing (-5-10%)")
        recommended_price = analysis['stats']['avg_price'] * 0.925
        print(f"     → Suggested price: ${recommended_price:.2f}")
    else:
        print(f"  💡 RECOMMENDATION: Maintain current pricing")
    print()


# In[70]:


# Create pricing optimization visualization
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Price vs Rating by Cluster with optimal zones
ax1 = axes[0, 0]
for cluster_id in range(3):
    cluster_data = top_products_df[top_products_df['cluster'] == cluster_id]
    ax1.scatter(cluster_data['price'], cluster_data['average_rating'], 
               label=f'Cluster {cluster_id+1}', s=60, alpha=0.6, edgecolors='black', linewidth=0.5)

# Add optimal pricing zones
ax1.axhspan(4.7, 5.0, alpha=0.2, color='green', label='Premium Zone (>4.7)')
ax1.axhspan(4.5, 4.7, alpha=0.2, color='yellow', label='Standard Zone')
ax1.set_xlabel('Price ($)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Average Rating', fontsize=11, fontweight='bold')
ax1.set_title('Pricing Strategy Map: Identify Opportunities', fontsize=12, fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)


# In[71]:


# Price distribution with recommended adjustments
ax2 = axes[0, 1]
for cluster_id in range(3):
    cluster_data = top_products_df[top_products_df['cluster'] == cluster_id]
    ax2.hist(cluster_data['price'], bins=15, alpha=0.5, label=f'Cluster {cluster_id+1}')
    median = cluster_data['price'].median()
    ax2.axvline(median, linestyle='--', linewidth=2, label=f'C{cluster_id+1} Median')

ax2.set_xlabel('Price ($)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Frequency', fontsize=11, fontweight='bold')
ax2.set_title('Price Distribution Analysis', fontsize=12, fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)


# In[72]:


# Value score vs Price - identify underpriced products
ax3 = axes[1, 0]
scatter = ax3.scatter(top_products_df['price'], top_products_df['value_score'], 
                     c=top_products_df['average_rating'], s=80, alpha=0.6, 
                     cmap='RdYlGn', edgecolors='black', linewidth=0.5)
ax3.set_xlabel('Price ($)', fontsize=11, fontweight='bold')
ax3.set_ylabel('Value Score', fontsize=11, fontweight='bold')
ax3.set_title('Identify Underpriced Products (High Value Score)', fontsize=12, fontweight='bold')
plt.colorbar(scatter, ax=ax3, label='Rating')
ax3.grid(True, alpha=0.3)

# Highlight top 10 underpriced products
top_underpriced = top_products_df.nlargest(10, 'value_score')
ax3.scatter(top_underpriced['price'], top_underpriced['value_score'], 
           s=200, facecolors='none', edgecolors='red', linewidths=3, 
           label='Top 10 Underpriced')
ax3.legend()


# In[73]:


# Revenue optimization potential
ax4 = axes[1, 1]
# Calculate potential revenue impact
top_products_df['current_revenue_estimate'] = top_products_df['price'] * top_products_df['review_count']

# Simulate optimized pricing
def optimize_price(row):
    if row['average_rating'] >= 4.7 and row['price'] < 50:
        return row['price'] * 1.15  # 15% increase
    elif row['average_rating'] < 4.6:
        return row['price'] * 0.95  # 5% decrease
    else:
        return row['price']

top_products_df['optimized_price'] = top_products_df.apply(optimize_price, axis=1)
top_products_df['optimized_revenue_estimate'] = top_products_df['optimized_price'] * top_products_df['review_count']

revenue_comparison = pd.DataFrame({
    'Current': top_products_df.groupby('cluster')['current_revenue_estimate'].sum(),
    'Optimized': top_products_df.groupby('cluster')['optimized_revenue_estimate'].sum()
})

revenue_comparison.plot(kind='bar', ax=ax4, color=['#FF6B6B', '#4ECDC4'])
ax4.set_xlabel('Cluster', fontsize=11, fontweight='bold')
ax4.set_ylabel('Estimated Revenue', fontsize=11, fontweight='bold')
ax4.set_title('Revenue Impact: Current vs Optimized Pricing', fontsize=12, fontweight='bold')
ax4.set_xticklabels([f'Cluster {i+1}' for i in range(3)], rotation=0)
ax4.legend(['Current Revenue', 'Optimized Revenue'])
ax4.grid(True, alpha=0.3, axis='y')

# Add percentage increase annotations
for i, (curr, opt) in enumerate(zip(revenue_comparison['Current'], revenue_comparison['Optimized'])):
    pct_increase = ((opt - curr) / curr) * 100
    ax4.text(i, opt, f'+{pct_increase:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('pricing_optimization_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n💰 REVENUE IMPACT ANALYSIS:")
total_current = revenue_comparison['Current'].sum()
total_optimized = revenue_comparison['Optimized'].sum()
total_increase = ((total_optimized - total_current) / total_current) * 100
print(f"  Current Estimated Revenue: ${total_current:,.0f}")
print(f"  Optimized Estimated Revenue: ${total_optimized:,.0f}")
print(f"  Potential Increase: {total_increase:.2f}%")
print(f"  Potential Additional Revenue: ${total_optimized - total_current:,.0f}")


# ## Inventory Management & Stock Optimization Case study

# In[79]:


print("\n" + "=" * 76)
print(" Inventory Management & Stock Optimization")
print("=" * 80)


# In[80]:


# Calculate inventory priority score
top_products_df['inventory_priority'] = (
    top_products_df['average_rating'] * 0.4 + 
    (top_products_df['review_count'] / top_products_df['review_count'].max()) * 0.3 +
    top_products_df['value_score'] * 0.3
)


# In[81]:


# Categorize products for inventory decisions
def categorize_inventory_action(row):
    if row['inventory_priority'] > top_products_df['inventory_priority'].quantile(0.75):
        return 'High Priority - Increase Stock'
    elif row['inventory_priority'] > top_products_df['inventory_priority'].quantile(0.50):
        return 'Medium Priority - Maintain Stock'
    elif row['inventory_priority'] > top_products_df['inventory_priority'].quantile(0.25):
        return 'Low Priority - Reduce Stock'
    else:
        return 'Consider Discontinuing'

top_products_df['inventory_action'] = top_products_df.apply(categorize_inventory_action, axis=1)


# In[83]:


# Analyze inventory recommendations
inventory_summary = top_products_df['inventory_action'].value_counts()

print("\n INVENTORY RECOMMENDATIONS:\n")
for action, count in inventory_summary.items():
    percentage = (count / len(top_products_df)) * 100
    print(f"{action}: {count} products ({percentage:.1f}%)")
    
    # Show example products
    examples = top_products_df[top_products_df['inventory_action'] == action].nlargest(3, 'inventory_priority')
    print("  Top 3 products:")
    for idx, row in examples.iterrows():
        print(f"    - {row['title'][:50]}...")
        print(f"      Price: ${row['price']:.2f}, Rating: ⭐{row['average_rating']:.2f}, Priority: {row['inventory_priority']:.3f}")
    print()


# In[84]:


# Create inventory management visualization
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Inventory priority heatmap
ax1 = axes[0, 0]
scatter = ax1.scatter(top_products_df['price'], top_products_df['review_count'], 
                     c=top_products_df['inventory_priority'], s=100, alpha=0.6, 
                     cmap='RdYlGn', edgecolors='black', linewidth=0.5)
ax1.set_xlabel('Price ($)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Review Count', fontsize=11, fontweight='bold')
ax1.set_title('Inventory Priority Map', fontsize=12, fontweight='bold')
ax1.set_yscale('log')
plt.colorbar(scatter, ax=ax1, label='Priority Score')
ax1.grid(True, alpha=0.3)


# In[85]:


# Inventory action distribution
ax2 = axes[0, 1]
action_colors = {'High Priority - Increase Stock': '#2ECC71', 
                'Medium Priority - Maintain Stock': '#F39C12',
                'Low Priority - Reduce Stock': '#E74C3C',
                'Consider Discontinuing': '#95A5A6'}
colors = [action_colors[action] for action in inventory_summary.index]
wedges, texts, autotexts = ax2.pie(inventory_summary.values, labels=inventory_summary.index, 
                                    autopct='%1.1f%%', startangle=90, colors=colors)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
ax2.set_title('Inventory Action Distribution', fontsize=12, fontweight='bold')


# In[86]:


# Category-wise inventory needs
ax3 = axes[1, 0]
category_inventory = pd.crosstab(top_products_df['category'], top_products_df['inventory_action'])
category_inventory.plot(kind='bar', stacked=True, ax=ax3, color=list(action_colors.values()))
ax3.set_xlabel('Category', fontsize=11, fontweight='bold')
ax3.set_ylabel('Number of Products', fontsize=11, fontweight='bold')
ax3.set_title('Inventory Needs by Category', fontsize=12, fontweight='bold')
ax3.tick_params(axis='x', rotation=45)
ax3.legend(title='Action', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
ax3.grid(True, alpha=0.3, axis='y')


# In[87]:


# Stock level recommendations
ax4 = axes[1, 1]
# Create recommended stock levels (simplified model)
top_products_df['recommended_stock'] = top_products_df['review_count'] / 10  # Simplified ratio

stock_by_cluster = top_products_df.groupby('cluster')['recommended_stock'].sum()
stock_by_cluster.plot(kind='bar', ax=ax4, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
ax4.set_xlabel('Cluster', fontsize=11, fontweight='bold')
ax4.set_ylabel('Recommended Stock Units', fontsize=11, fontweight='bold')
ax4.set_title('Recommended Stock Levels by Cluster', fontsize=12, fontweight='bold')
ax4.set_xticklabels([f'Cluster {i+1}' for i in range(3)], rotation=0)
ax4.grid(True, alpha=0.3, axis='y')

# Add value annotations
for i, val in enumerate(stock_by_cluster):
    ax4.text(i, val, f'{val:.0f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('inventory_optimization_analysis.png', dpi=300, bbox_inches='tight')
plt.show()


# ## Advanced Data Formats

# In[88]:


import pandas as pd
import numpy as np
import json
import pickle
import sqlite3
import warnings
warnings.filterwarnings('ignore')


# In[89]:


print("=" * 80)
print("ADVANCED DATA FORMATS ")
print("Beyond CSV and Parquet")
print("=" * 80)


# In[90]:


# Create sample e-commerce data for demonstrations
np.random.seed(42)
n_products = 100

sample_data = pd.DataFrame({
    'product_id': [f'PROD_{i:04d}' for i in range(n_products)],
    'title': [f'Product {i}' for i in range(n_products)],
    'price': np.random.uniform(10, 200, n_products),
    'average_rating': np.random.uniform(4.5, 5.0, n_products),
    'review_count': np.random.randint(10, 1000, n_products),
    'category': np.random.choice(['Electronics', 'Accessories', 'Audio', 'Computing'], n_products),
    'in_stock': np.random.choice([True, False], n_products, p=[0.8, 0.2]),
    'last_updated': pd.date_range('2024-01-01', periods=n_products, freq='D')
})

print(f"\n✅ Created sample dataset with {len(sample_data)} products")
print(f"📊 Columns: {list(sample_data.columns)}")


# ### Format 1: JSON (JavaScript Object Notation)

# In[91]:


print("\n" + "🔹 " + "=" * 76)
print("FORMAT 1: JSON - JavaScript Object Notation")
print("=" * 80)

print("\n📝 Overview:")
print("   - Human-readable text format")
print("   - Hierarchical/nested data structures")
print("   - Universal web standard")
print("   - Language-independent")

# Save as JSON
sample_data.to_json('products.json', orient='records', indent=2)
print("\n✅ Saved: products.json (records orientation)")

# Different JSON orientations
sample_data.head(3).to_json('products_split.json', orient='split', indent=2)
sample_data.head(3).to_json('products_index.json', orient='index', indent=2)
sample_data.head(3).to_json('products_columns.json', orient='columns', indent=2)
sample_data.head(3).to_json('products_values.json', orient='values')

print("\n📊 JSON Orientations Available:")
print("   1. 'records' - List of dictionaries (most common)")
print("   2. 'split' - Dict with index, columns, data")
print("   3. 'index' - Dict with index as keys")
print("   4. 'columns' - Dict with columns as keys")
print("   5. 'values' - Just the values array")


# In[92]:


# Read JSON back
json_data = pd.read_json('products.json', orient='records')
print(f"\n✅ Read back: {len(json_data)} records")


# 
# ### Format 2: Pickle (Python-specific binary format)

# In[93]:


print("\n" + "🔹 " + "=" * 76)
print("FORMAT 2: PICKLE - Python Binary Serialization")
print("=" * 80)

print("\n📝 Overview:")
print("   - Python-native binary format")
print("   - Preserves Python objects exactly")
print("   - Fast serialization/deserialization")
print("   - NOT secure or cross-language")

# Save as pickle
sample_data.to_pickle('products.pkl')
print("\n✅ Saved: products.pkl")


# In[94]:


# Read back
loaded_df = pd.read_pickle('products.pkl')
print(f"\n✅ Read back: {len(loaded_df)} records")


# 
# ### Format 3: HDF5 (Hierarchical Data Format)

# In[96]:


print("\n" + "🔹 " + "=" * 76)
print("FORMAT 3: HDF5 - Hierarchical Data Format 5")
print("=" * 80)

print("\n📝 Overview:")
print("   - Designed for large scientific datasets")
print("   - Hierarchical structure (like file system)")
print("   - Efficient compression")
print("   - Partial reading (don't load entire file)")

try:
    # Save as HDF5
    sample_data.to_hdf('products.h5', key='products', mode='w', format='table')
    print("\n✅ Saved: products.h5 (table format)")
    
    # Multiple datasets in one file
    with pd.HDFStore('ecommerce_data.h5', mode='w') as store:
        store['products'] = sample_data
        store['high_rated'] = sample_data[sample_data['average_rating'] >= 4.7]
        store['low_stock'] = sample_data[sample_data['in_stock'] == False]
        store['metadata'] = pd.DataFrame({
            'created': ['2024-01-01'],
            'total_products': [len(sample_data)]
        })
    
    print("✅ Created multi-dataset HDF5 file with 4 tables")
    
    # Read specific dataset
    high_rated = pd.read_hdf('ecommerce_data.h5', key='high_rated')
    print(f"\n✅ Read 'high_rated' table: {len(high_rated)} records")
    
    # Query without loading entire file
    with pd.HDFStore('ecommerce_data.h5', mode='r') as store:
        print(f"\n📚 Available tables: {store.keys()}")
        
        # Query with condition
        expensive = store.select('products', where='price > 100')
        print(f"✅ Queried products with price > 100: {len(expensive)} records")
    
    print("\n💡 Use Cases:")
    print("   ✓ Large scientific datasets")
    print("   ✓ Time-series data")
    print("   ✓ Multi-dimensional arrays")
    print("   ✓ Simulation results")
    print("   ✓ Sensor/IoT data")
    
    print("\n⚖️ Pros vs Cons:")
    print("   PROS:")
    print("   + Very fast I/O")
    print("   + Efficient compression")
    print("   + Partial reading")
    print("   + Multiple datasets per file")
    print("   CONS:")
    print("   - Requires tables library")
    print("   - More complex API")
    print("   - File locking issues")
    print("   - Not as portable as Parquet")

except ImportError:
    print("\n⚠️  HDF5 requires 'tables' package: pip install tables")


# ### Format 4: Feather (Apache Arrow IPC)

# In[97]:


print("\n" + "🔹 " + "=" * 76)
print("FORMAT 4: FEATHER - Apache Arrow IPC Format")
print("=" * 80)

print("\n📝 Overview:")
print("   - Designed for fast DataFrame I/O")
print("   - Language-agnostic (R, Python, etc.)")
print("   - Columnar format")
print("   - Zero-copy reads")

try:
    # Save as Feather
    sample_data.to_feather('products.feather')
    print("\n✅ Saved: products.feather")
    
    # Read back
    feather_data = pd.read_feather('products.feather')
    print(f"✅ Read back: {len(feather_data)} records")
    
    # Feather v2 with compression
    sample_data.to_feather('products_compressed.feather', compression='lz4')
    print("✅ Saved with LZ4 compression")
    
    print("\n💡 Use Cases:")
    print("   ✓ Temporary file storage")
    print("   ✓ Inter-process communication")
    print("   ✓ R ↔ Python data exchange")
    print("   ✓ Fast prototyping")
    
    print("\n⚖️ Pros vs Cons:")
    print("   PROS:")
    print("   + Extremely fast")
    print("   + Language-agnostic")
    print("   + Preserves data types")
    print("   + Zero-copy reads")
    print("   CONS:")
    print("   - Limited compression")
    print("   - No query capabilities")
    print("   - Less mature than Parquet")
    print("   - Not for long-term storage")

except Exception as e:
    print(f"\n⚠️  Feather error: {e}")


# ### Format 5: SQLite Database

# In[98]:


print("\n" + "🔹 " + "=" * 76)
print("FORMAT 5: SQLite - Embedded Relational Database")
print("=" * 80)

print("\n📝 Overview:")
print("   - Full SQL database in a single file")
print("   - No server required")
print("   - ACID transactions")
print("   - Cross-platform")

# Create SQLite database
conn = sqlite3.connect('ecommerce.db')

# Save DataFrame to SQLite
sample_data.to_sql('products', conn, if_exists='replace', index=False)
print("\n✅ Created SQLite database: ecommerce.db")
print("✅ Saved table: products")

# Create additional tables
high_rated = sample_data[sample_data['average_rating'] >= 4.7]
high_rated.to_sql('premium_products', conn, if_exists='replace', index=False)
print("✅ Created table: premium_products")

# Execute SQL queries
query = """
SELECT category, 
       COUNT(*) as product_count,
       AVG(price) as avg_price,
       AVG(average_rating) as avg_rating
FROM products
GROUP BY category
ORDER BY avg_price DESC
"""

category_stats = pd.read_sql_query(query, conn)
print("\n📊 SQL Query Results (Category Statistics):")
print(category_stats.to_string(index=False))

# Complex JOIN query
conn.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product_id TEXT,
    quantity INTEGER,
    revenue REAL,
    sale_date DATE
)
""")

# Insert sample sales data
sales_data = pd.DataFrame({
    'product_id': sample_data['product_id'].sample(20).values,
    'quantity': np.random.randint(1, 100, 20),
    'revenue': np.random.uniform(100, 10000, 20),
    'sale_date': pd.date_range('2024-01-01', periods=20, freq='D')
})
sales_data.to_sql('sales', conn, if_exists='replace', index=False)

# JOIN query
join_query = """
SELECT p.product_id, p.title, p.category, 
       SUM(s.quantity) as total_quantity,
       SUM(s.revenue) as total_revenue
FROM products p
JOIN sales s ON p.product_id = s.product_id
GROUP BY p.product_id, p.title, p.category
ORDER BY total_revenue DESC
LIMIT 10
"""

top_sellers = pd.read_sql_query(join_query, conn)
print("\n📊 Top 10 Products by Revenue:")
print(top_sellers.to_string(index=False))

conn.close()

print("\n💡 Use Cases:")
print("   ✓ Application databases")
print("   ✓ Data warehousing (small scale)")
print("   ✓ Analytics with SQL queries")
print("   ✓ Mobile/embedded applications")
print("   ✓ Testing and prototyping")

print("\n⚖️ Pros vs Cons:")
print("   PROS:")
print("   + Full SQL support")
print("   + No server setup")
print("   + ACID compliant")
print("   + Indexes and views")
print("   + Built into Python")
print("   CONS:")
print("   - Single writer limitation")
print("   - Not for massive datasets")
print("   - No user management")
print("   - Limited concurrent access")


# ### Format 8: MessagePack

# In[99]:


print("\n" + "🔹 " + "=" * 76)
print("FORMAT 8: MessagePack - Efficient Binary Serialization")
print("=" * 80)

print("\n📝 Overview:")
print("   - Binary JSON alternative")
print("   - Smaller and faster than JSON")
print("   - Multiple language support")
print("   - Streaming capable")

try:
    import msgpack
    
    # Convert to dict and serialize
    data_dict = sample_data.head(10).to_dict('records')
    
    # Pack to MessagePack
    packed = msgpack.packb(data_dict)
    
    with open('products.msgpack', 'wb') as f:
        f.write(packed)
    
    print(f"\n✅ Saved: products.msgpack ({len(packed)} bytes)")
    
    # Unpack
    with open('products.msgpack', 'rb') as f:
        unpacked = msgpack.unpackb(f.read())
    
    print(f"✅ Read back: {len(unpacked)} records")
    
    # Compare sizes
    import os
    json_size = os.path.getsize('products.json')
    msgpack_size = os.path.getsize('products.msgpack')
    print(f"\n📊 Size Comparison:")
    print(f"   JSON: {json_size:,} bytes")
    print(f"   MessagePack: {msgpack_size:,} bytes")
    print(f"   Reduction: {(1 - msgpack_size/json_size)*100:.1f}%")
    
    print("\n💡 Use Cases:")
    print("   ✓ Network protocols")
    print("   ✓ IPC (inter-process communication)")
    print("   ✓ Cache storage (Redis)")
    print("   ✓ Real-time applications")
    
    print("\n⚖️ Pros vs Cons:")
    print("   PROS:")
    print("   + Faster than JSON")
    print("   + Smaller than JSON")
    print("   + Binary format")
    print("   + Streaming support")
    print("   CONS:")
    print("   - Not human-readable")
    print("   - Less widespread than JSON")
    print("   - Requires library")

except ImportError:
    print("\n⚠️  MessagePack requires 'msgpack' package: pip install msgpack")


# ### DATA FORMAT COMPARISON

# In[101]:


print("\n" + "=" * 80)
print("DATA FORMAT COMPARISON")
print("=" * 80)


# In[102]:


import os

# Compare file sizes
formats_comparison = []

file_formats = [
    ('CSV', 'products.csv', 'Text'),
    ('JSON', 'products.json', 'Text'),
    ('Pickle', 'products.pkl', 'Binary'),
    ('Feather', 'products.feather', 'Binary'),
    ('Parquet', 'products.parquet', 'Binary'),
    ('SQLite', 'ecommerce.db', 'Binary'),
    ('MessagePack', 'products.msgpack', 'Binary')
]


# In[103]:


# Create CSV and Parquet for comparison
sample_data.to_csv('products.csv', index=False)
sample_data.to_parquet('products.parquet', index=False)

print("\n📊 FILE SIZE COMPARISON:\n")
print(f"{'Format':<15} {'Size (KB)':<12} {'Type':<10} {'Compression'}")
print("-" * 55)

for name, filename, file_type in file_formats:
    if os.path.exists(filename):
        size_kb = os.path.getsize(filename) / 1024
        compression = "✓" if file_type == 'Binary' else "✗"
        formats_comparison.append({
            'format': name,
            'size_kb': size_kb,
            'type': file_type
        })
        print(f"{name:<15} {size_kb:>10.2f}  {file_type:<10} {compression:^12}")


# In[104]:


# Create comparison DataFrame
comparison_df = pd.DataFrame(formats_comparison)
if not comparison_df.empty:
    print(f"\n💡 Most Efficient: {comparison_df.loc[comparison_df['size_kb'].idxmin(), 'format']}")
    print(f"   Size: {comparison_df['size_kb'].min():.2f} KB")


# ### FORMAT SELECTION GUIDE

# In[106]:


selection_guide = """
┌─────────────────────┬──────────────────────────────────────────────┐
│ Use Case            │ Recommended Format                           │
├─────────────────────┼──────────────────────────────────────────────┤
│ Data Exchange       │ JSON (universal), CSV (simple)               │
│ API Responses       │ JSON, MessagePack (performance)              │
│ Configuration       │ YAML (readable), JSON (simple)               │
│ Data Archival       │ Parquet (analytics), Avro (Hadoop)          │
│ ML Models           │ Pickle (Python), ONNX (cross-platform)      │
│ Big Data Analytics  │ Parquet, ORC, Delta Lake                    │
│ Streaming Data      │ Avro, Protocol Buffers, JSONL               │
│ Mobile Apps         │ Protocol Buffers, MessagePack               │
│ Data Warehousing    │ Parquet, ORC, Delta Lake                    │
│ Web Applications    │ JSON, MessagePack                           │
│ IoT/Sensors         │ Protocol Buffers, MessagePack, Avro         │
│ Scientific Data     │ HDF5, NetCDF                                │
│ Temporary Storage   │ Feather, Pickle                             │
│ Enterprise Systems  │ XML, Parquet, Avro                          │
└─────────────────────┴──────────────────────────────────────────────┘

🎯 QUICK DECISION TREE:

1. Need human readability?
   YES → JSON, YAML, CSV
   NO  → Continue

2. Need cross-language support?
   YES → JSON, Parquet, Avro, Protocol Buffers
   NO  → Pickle (Python-only is fine)

3. Dataset size > 1GB?
   YES → Parquet, ORC, Delta Lake
   NO  → Continue

4. Need schema evolution?
   YES → Avro, Protocol Buffers, Delta Lake
   NO  → Continue

5. Need ACID transactions?
   YES → SQLite (small), Delta Lake (large)
   NO  → Continue

6. Primary use is analytics?
   YES → Parquet (columnar)
   NO  → Avro, MessagePack (row-based)

7. Real-time/streaming data?
   YES → Avro, Protocol Buffers, MessagePack
   NO  → Standard formats (CSV, JSON, Parquet)
"""


# In[107]:


print(selection_guide)


# In[109]:


print("\n" + "=" * 80)
print("FORMATS DEMONSTRATION COMPLETE!")
print("=" * 80)

print("\n📁 Files Created:")
created_files = [
    'products.json', 'products_split.json', 'products.jsonl',
    'products.pkl', 'complex_object.pkl',
    'products.feather', 'products_compressed.feather',
    'ecommerce.db',
    'products.xml', 'products.yaml',
    'products.msgpack',
    'products.csv', 'products.parquet'
]

for i, filename in enumerate(created_files, 1):
    if os.path.exists(filename):
        size = os.path.getsize(filename) / 1024
        print(f"   {i:2d}. {filename:<30} ({size:>8.2f} KB)")


print("Ready to explore Python APIs and SDKs for further studies!")


# In[ ]:





# In[ ]:





# ## 📁 Be Sure to Download Your Great Work:
# You should see these in the file directory on the left:
# - [ ] This Jupyter Notebook with your cell outputs included
# - [ ] Your `user_inputs.txt` file with your answers to all reflection questions
# - [ ] Your `top_products.csv` dataset
# - [ ] Your `top_products.parquet` dataset
