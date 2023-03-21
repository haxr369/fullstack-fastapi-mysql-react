import axios from "axios";
async function SearchPlantAPI(query) {
    try{
        console.log("API query : "+query);
        const result = await axios.get(`/api/v1/search/searchquery?query=${query}`);
        //console.log(result)
        return result
        
    }
    catch (ex){
        return [];
    } 
}

export default SearchPlantAPI;