function Microphone({ setText }) {
  const startSpeech = async () => {
    const res = await fetch("http://localhost:5000/speech");
    const data = await res.json();
    setText(data.original_text);
  };

  return (
    <button onClick={startSpeech}>
      🎙 Speak
    </button>
  );
}

export default Microphone;
