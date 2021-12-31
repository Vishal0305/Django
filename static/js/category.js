const BASE_URL = 'http:127.0.0.1:8000/app';
console.log('hoii')
const getItems = async function(id){
    try {
      const response = await axios.get(`?category=${id}`);
      console.log(response.data)
      return "success";
    } catch (errors) {
      console.error(errors);
      return "failed";
    }
};