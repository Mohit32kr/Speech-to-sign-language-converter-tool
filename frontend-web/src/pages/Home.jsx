import { useState } from "react";
import Microphone from "../components/Microphone";
import SignPlayer from "../components/Signplayer";
import { convertText } from "../services/api";

function Home() {
  const [text, setText] = useState("");
  const [signs, setSigns] = useState([]);

  const handleConvert = async () => {
    const response = await convertText(text);
    setSigns(response.signs);
  };

  return (
    <div className="container">
      <Microphone setText={setText} />

      <textarea
        placeholder="Recognized or typed text..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button onClick={handleConvert}>Convert to Sign</button>

      <SignPlayer signs={signs} />
    </div>
  );
}

export default Home;
