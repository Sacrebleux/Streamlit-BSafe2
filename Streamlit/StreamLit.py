import streamlit as st



st.header("Bliksemziel Safe", divider="blue")
col1, col2, col3, col4, col5, col6 = st.columns(6)




with col1:
    Citrine = st.button(
        "Citrine",
        use_container_width = True,
    )
with col2:
    Sapphire = st.button(
        "Sapphire",
        use_container_width = True,
    )
with col3:
    Opal = st.button(
        "Opal",
        use_container_width = True,
    )
with col4:
    Hematite = st.button(
        "Hematite",
        use_container_width = True,
    )
with col5:
    Diamond = st.button(
        "Diamond",
        use_container_width = True,
    )
with col6:
    Lapis = st.button(
        "Lapis",
        use_container_width = True,
    )
with col1:
    Pearl = st.button(
        "Pearl",
        use_container_width = True,
    )
with col2:
    Nephrite = st.button(
        "Nephrite",
        use_container_width = True,
    )
with col3:
    Topaz = st.button(
        "Topaz",
        use_container_width = True,
    )
with col4:
    Bloodstone = st.button(
        "Bloodstone",
        use_container_width = True,
    )
with col5:
    Ruby = st.button(
        "Ruby",
        use_container_width = True,
    )
with col6:
    Jade = st.button(
        "Jade",
        use_container_width = True,
    )
with col1:
    Garnet = st.button(
        "Garnet",
        use_container_width = True,
    )
with col2:
    Moonstone = st.button(
        "Moonstone",
        use_container_width = True,
    )
with col3:
    Wolframite = st.button(
        "Wolframite",
        use_container_width = True,
    )
with col4:
    Zircon = st.button(
        "Zircon",
        use_container_width = True,
    )
with col5:
    Emerald = st.button(
        "Emerald",
        use_container_width = True,
    )
with col6:
    Amber = st.button(
        "Amber",
        use_container_width = True,
    )


if "disabled" not in st.session_state:
    st.session_state["disabled"] = False

def disable():
    st.session_state["disabled"] = True

info = st.text_input(
    "Password",
    disabled = st.session_state.disabled,
    on_change = disable,
    label_visibility = 'hidden',
    max_chars = 5,
)

def enable():
    st.session_state["disabled"] = False


Reset = st.button(
    "Reset",
    on_click = enable,
)

if info.lower() == "storm":
    st.write("The safe has opened")
#"I am the voice of the sky, the herald of the storm. Press my name, and I shall open the way."

if info.lower() != "storm" and Reset:
    if info.lower() == "":
        st.write("")
    else:
        st.write("Take 1d4 Force Damage")


if Amber:
    st.write("You feel a sense pulling you up.")

if Bloodstone:
    st.write("You feel your blood pulling you in 3 different directions.")

if Opal:
    st.write("You feel your a sense of calm")

if Citrine:
    st.write("You feel a sense of unbalance pulling you to the right.")

if Sapphire:
    st.write("You feel a sense of focus.")

if Hematite:
    st.write("You feel a sense of grounding pulling you in 3 different directions.")

if Diamond:
    st.write("You feel a sense of energy pulling you down.")

if Lapis:
    st.write("You feel a sense of wisdom pulling you to left.")

if Pearl:
    st.write("You feel a sense of clarity pulling you in 3 different directions.")

if Nephrite:
    st.write("You feel a sense of prosperity pulling you in 4 different directions.")

if Topaz:
    st.write("You feel a sense of confidence.")

if Ruby:
    st.write("You feel a sense of strength.")

if Jade:
    st.write("You feel a sense of nature pulling you to the right.")

if Garnet:
    st.write("You feel a sense of purity to your right.")

if Moonstone:
    st.write("You feel a sense of inspiration.")

if Wolframite:
    st.write("You feel a sense of endurance pulling you in 2 different directions.")

if Zircon:
    st.write("You feel a sense of soothing pulling you in 2 different directions.")

if Emerald:
    st.write("You feel a sense of vitality pulling you up,")
