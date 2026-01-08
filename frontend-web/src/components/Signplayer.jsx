function SignPlayer({ signs }) {
  return (
    <div className="sign-container">
      {signs.map((sign, index) => (
        <video
          key={index}
          src={`http://localhost:5000/static/signs/${sign}`}
          controls
          autoPlay
        />
      ))}
    </div>
  );
}

export default SignPlayer;
