import streamlit as st

# Website Layout & Theme Setup
st.set_page_config(page_title="AI Message Writer", page_icon="✍️", layout="centered")

st.title("✍️ AI Professional Email & Message Generator")
st.write("Shahid Alam ka banaya hua Smart Communication Tool")
st.write("---")

# User se input lena
user_prompt = st.text_area("Aapko kya message bhejna hai? (Apni bhasha/Hinglish me likhein)", 
                           placeholder="Example: Boss ko bolo kal chutti chahiye kyunki shaadi me jana hai")

# Tone select karne ke liye dropdown
tone = st.selectbox("Message ki tone kaisi honi chahiye?", ["Professional / Office", "Casual / Friendly", "Urgent / Short"])

# Button check
if st.button("Generate Professional Message ✨"):
    if user_prompt.strip() == "":
        st.warning("Pehle kuch likhiye toh sahi!")
    else:
        st.subheader("📝 Aapka AI Generated Message:")
        
        # Simple rule-based formatting template jo user ke input ko professional text me wrap karega
        # (Aage chal kar isme hum real AI model bhi connect kar sakte hain!)
        clean_input = user_prompt.replace("kal", "tomorrow").replace("chutti", "leave").replace("shaadi", "wedding")
        
        if tone == "Professional / Office":
            generated_text = f"Dear Sir/Madam,\n\nI am writing to formally request assistance regarding: '{clean_input}'. Kindly review this request and let me know the next steps.\n\nBest regards,\n[Your Name]"
        elif tone == "Urgent / Short":
            generated_text = f"Hello,\n\nThis is an urgent notification regarding: '{clean_input}'. Please update me on this as soon as possible.\n\nThank you,\n[Your Name]"
        else:
            generated_text = f"Hey there,\n\nJust wanted to reach out and drop a quick note about: '{clean_input}'. Let me know what you think!\n\nCheers,\n[Your Name]"
            
        # Screen par output dikhana
        st.text_area("Ise yahan se Copy karein:", value=generated_text, height=200)
        st.success("Aapka message taiyar hai! Copy karke use karein. 🚀")
              
