import requests,streamlit as st
st.set_page_config(page_title="AstraMind AI",page_icon="🧠",layout="wide")
api=st.sidebar.text_input("API URL","http://localhost:8000")
st.title("🧠 AstraMind AI")
st.caption("Agentic enterprise intelligence • Hybrid RAG • Evidence-backed answers")
with st.sidebar:
    st.subheader("Knowledge base")
    uploads=st.file_uploader("Upload PDF, DOCX, TXT, MD or CSV",type=["pdf","docx","txt","md","csv"],accept_multiple_files=True)
    if st.button("Index documents"):
        if uploads:
            multipart=[("files",(f.name,f.getvalue(),f.type or "application/octet-stream")) for f in uploads]
            try:
                r=requests.post(f"{api}/ingest",files=multipart,timeout=300); r.raise_for_status(); st.success(r.json())
            except Exception as e: st.error(str(e))
        else: st.warning("Choose documents first.")
    if st.button("Show metrics"):
        try: st.json(requests.get(f"{api}/metrics",timeout=10).json())
        except Exception as e: st.error(str(e))
q=st.text_area("Ask your enterprise knowledge base",height=110,placeholder="Summarise the incident response procedure and cite sources.")
k=st.slider("Evidence chunks",1,10,5)
if st.button("Ask AstraMind",type="primary"):
    if len(q.strip())<3: st.warning("Enter a longer question.")
    else:
        try:
            with st.spinner("Retrieving evidence and generating answer..."):
                r=requests.post(f"{api}/ask",json={"question":q,"top_k":k},timeout=180); r.raise_for_status(); data=r.json()
            st.subheader("Answer"); st.write(data["answer"])
            st.caption(f"Path: {data['tool']} | Usage: {data.get('usage',{})}")
            st.subheader("Evidence")
            for s in data.get("sources",[]):
                with st.expander(f"[{s['id']}] {s['source']}"): st.write(s["excerpt"])
            rating=st.radio("Rate answer",[1,2,3,4,5],horizontal=True)
            comment=st.text_input("Feedback (optional)")
            if st.button("Submit feedback"):
                requests.post(f"{api}/feedback",json={"question":q,"answer":data["answer"],"rating":rating,"comment":comment},timeout=10).raise_for_status()
                st.success("Feedback saved.")
        except Exception as e: st.error(f"{e}. Ensure API and LLM endpoint are running.")
