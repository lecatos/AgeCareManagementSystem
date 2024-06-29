import {reactive, ref} from "vue";
import axios from "axios";
import {useRouter} from "vue-router";


export const logged_user = ref({
    is_logged: false,
    username: "Guest",
    logout: function(){
        axios.post("/api/user/logout").then(()=>{
            this.username = "Guest";
            this.is_logged = false;
        })
    },
})