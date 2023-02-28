import React from 'react';

const PlantItem = ({ plant }) => {
  return (
    <div className="plant-item">
      <img src={plant.image} alt={plant.species} className="plant-image" />
      <div className="plant-info">
        <h2>{plant.species}</h2>
        <p>Genus: {plant.genus}</p>
        <p>Family: {plant.family}</p>
      </div>
    </div>
  );
};

export default PlantItem;