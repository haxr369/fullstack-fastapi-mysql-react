import React from 'react';
import PlantItem from './PlantItem';

const PlantList = ({ plants }) => {
  return (
    <div className="plant-list">
      {plants.map((plant) => (
        <PlantItem key={plant.id} plant={plant} />
      ))}
    </div>
  );
};

export default PlantList;