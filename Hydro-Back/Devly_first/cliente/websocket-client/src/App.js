import React, { useEffect, useState } from "react";
import * as websockets from "websockets";

const App = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    const socket = new websockets.WebSocket("ws://192.168.0.5:4000/"); // Ajusta la URL del servidor si es necesario

    socket.onopen = () => {
      console.log("Conexión WebSocket establecida");
    };

    socket.onmessage = (event) => {
      const jsonData = JSON.parse(event.data);
      setData(jsonData);
    };

    socket.onclose = () => {
      console.log("Conexión WebSocket cerrada");
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <div>
      <h1>Datos del Servidor WebSocket</h1>
      <p>WaterTem: {data.waterTem || ""}</p>
      <p>temperature: {data.temperature || ""}</p>
      <p>Humidity: {data.humedity || ""}</p>
      <p>Light: {data.light || ""}</p>
      <p>Ph: {data.pH || ""}</p>
      <p>Conduct: {data.conduct || ""}</p>
    </div>
  );
};

export default App;