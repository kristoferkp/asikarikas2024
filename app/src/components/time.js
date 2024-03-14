import React, { useState, useEffect } from 'react';

function Time() {
  const [temps, setTemps] = useState(null); // Declare temps state variable

  async function fetchData() {
    try {
      const response = await fetch('data.txt');
      const jsonData = await response.json();
      setTemps(jsonData); // Update state with jsonData
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error;
    }
  }

  useEffect(() => {
    // Call the fetchData function when the component mounts
    fetchData();
  }, []); // Empty dependency array ensures it only runs once when the component mounts

  const date = new Date();
  const showTime = date.getHours();

  return (
    <div className="App">
      <p>Kell: {showTime}</p>
      {temps && <p>Temperatuur: {Math.round(temps[showTime]).toFixed(2)} C</p>}
    </div>
  );
}

export default Time;
