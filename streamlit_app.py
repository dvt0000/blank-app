import streamlit as st


def main() -> None:
    """Render the Streamlit UI."""

    st.title("🎈 My new app")
    st.write(
        "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )


if __name__ == "__main__":
    if not st.runtime.exists():
        raise SystemExit(
            "Please run this app using 'streamlit run streamlit_app.py'"
        )
    main()
else:
    main()
