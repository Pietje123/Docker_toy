<script setup>
import { ref } from "vue";

// import UserInterface from './UserInterface.vue';
import ChangeUser from "./ChangeUser.vue";


defineProps({
    fields: {
        type: Object,
        required: true
    },
    fieldOrder: {
        type: Array,
        required: true
    },
    UIToggle: {
        type: Boolean,
        default: false
    }
});

let UIToggle = ref(false);

const emit = defineEmits(
    ['overlay-toggle']
)

function checkDate(date) {
    if ((new Date(date) !== "Invalid Date") && !isNaN(new Date(date)) && typeof(date) === 'string') {
        return (date.split(':')[0]).slice(0,-3)
    } else {
        return date
    }
};

function toggleUI(){
    UIToggle.value = !UIToggle.value;
}

</script>

<template>
    <ChangeUser v-if="UIToggle" v-bind="this.fields" @click="toggleUI"/>
    <tr id="vue-row" @click="toggleUI">
        <td v-for="field in fieldOrder">
            {{ checkDate(fields[field]) }}
        </td>
    </tr>
</template>

<style>
#vue-row:hover{
    background-color: rgb(207, 207, 207);
}
</style>