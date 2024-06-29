import {reactive, ref} from "vue";
import axios from "axios";
import {useRouter} from "vue-router";
import {computed} from 'vue';


export const serviceStore = ref({
    users: [],
    clients: [],
    refresh: async function(){
            this.users = (await axios.get("/api/user/list?limit=10000")).data.results
            this.clients = (await axios.get("/api/client/list?limit=10000")).data.results
    },
})