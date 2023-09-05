<script setup>
import { ref } from "vue";

const props = defineProps({
    username: String,
    birthdate: String,
})

const emit = defineEmits(
    ['new-user-added']
)

const username = ref(props.username);
const birthdate = ref(props.birthdate);

function confirmNewUser() {
    if ((this.username !== '') && (this.birthdate !== '')){
        emit('new-user-added', {'name': this.username, 'birthday' : this.birthdate});
    } else {
        alert('Add name and birthdate');
    };
    this.resetDefaults();

}

function resetDefaults() {
    this.username = props.username.value;
    this.birthdate = props.birthdate.value;
}

</script>

<template>
    <div class="overlay">
        <div id="user-form-div">
            <form>
                <input v-model="username" placeholder="Username"><br>
                <input type="date" v-model="birthdate">
            </form>
            <div>
                <button @click="confirmNewUser()">
                    Confirm
                </button>
            </div>
        </div>
    </div>
</template>

<style>
#user-form-div{
    border: 5px solid;
    border-color: rgba(215, 212, 212, 0.5);
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    padding: 10px;
    z-index: 2;
    /* color: white; */
}


.overlay {
    position: fixed; /* Sit on top of the page content */
    width: 100%; /* Full width (cover the whole page) */
    height: 100%; /* Full height (cover the whole page) */
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0,0,0,0.75); /* Black background with opacity */
    z-index: 1; /* Specify a stack order in case you're using a different order for other elements */
    cursor: pointer; /* Add a pointer on hover */
}
</style>