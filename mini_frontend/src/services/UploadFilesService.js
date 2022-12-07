import axios from "axios"


const baseurl = "http://127.0.0.1:5000"

class UploadFilesService {

  upload(file) {
    let formData = new FormData();
    formData.append("file", file);
    return axios.post(baseurl + "/upload", formData);
  }
  getFiles() {
    return axios.get(baseurl + "/files");
  }
}
export default new UploadFilesService();