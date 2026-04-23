import { useState } from 'react'

function SlopeCalculator() {
  const [x1, setX1] = useState('')
  const [x2, setX2] = useState('')
  const [y1, setY1] = useState('')
  const [y2, setY2] = useState('')
  const [slope, setSlope] = useState(null)

  const calculateSlope = async () => {
    try {
      const response = await fetch(
        `http://localhost:8000/api/v1/cartesian/slope?x1=${x1}&x2=${x2}&y1=${y1}&y2=${y2}`
      )
      const data = await response.json()
      setSlope(data.message)
    } catch (error) {
      console.error('Error calculating slope:', error)
    }
  }

  return (
    <div className="calculator">
      <input
        type="number"
        placeholder="x1"
        value={x1}
        onChange={(e) => setX1(e.target.value)}
      />
      <input
        type="number"
        placeholder="x2"
        value={x2}
        onChange={(e) => setX2(e.target.value)}
      />
      <input
        type="number"
        placeholder="y1"
        value={y1}
        onChange={(e) => setY1(e.target.value)}
      />
      <input
        type="number"
        placeholder="y2"
        value={y2}
        onChange={(e) => setY2(e.target.value)}
      />
      <button onClick={calculateSlope}>Calculate Slope</button>
      {slope !== null && <p>Slope: {slope}</p>}
    </div>
  )
}

export default SlopeCalculator