import {
    getHelloAPI,
} from '../api/image.js'


const Image = {
    actions: {
        getHello: async function({}) {
            let res = await getHelloAPI()
            if (res) {
                console.log(res);
                return res;
            }
        }
    }
}