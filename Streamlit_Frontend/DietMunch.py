import streamlit as st

st.set_page_config(
    page_title="🍲 DietMunch! 🥘👨‍⚕️",
    page_icon="👋",
)

# Title with Icon
st.title("🍏 Welcome to Diet Recommendation System! 🥦")

# Main Content
st.markdown(
    """
    ❤️ A diet recommendation 🍒 web application where you can generate your meal plan according to your needs 😋. 
    Whether you're looking to shed some pounds 🍸 or just eat healthier 🍵, our system provides personalized diet recommendations 🔥.
    """
)

# Additional Features Section
st.write("## 🌟 What I do Here 📊:")
st.write(
    """
    🥗 Personalized Recommendations: Discover recipes tailored to your taste preferences and dietary requirements.
    📋 Ingredient : Find ingredients for your recipes to suit your dietary restrictions or preferences.
    🥕 Nutritional Info: Access expert Nutritional info on every recipe.
    🍳 Community Recipes: Explore a vast collection of recipes shared by our vibrant community of food lovers.
    """
)

# Footer
st.markdown(
    """
    ---
    Built with ❤️
    """
)