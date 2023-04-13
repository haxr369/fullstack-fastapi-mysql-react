import React, { useState, useEffect } from 'react';
import axios from "axios";

const DetailPlantInfo = async (Species) => {
  /**
   * ^^^props^^^^
   * Species
   * onSearchDetail
   * 
   */
  try{
      console.log("Species name : "+Species);
      const result = await axios.get(`/api/v1/search/detailinfo?species=${Species}`);
      return result;
  }
  catch (ex){
    console.log(ex);
    return -1;
  } 
}
export default DetailPlantInfo;
