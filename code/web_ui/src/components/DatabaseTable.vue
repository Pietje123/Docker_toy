<script setup>
import { ref } from 'vue'

import ChangeUser from './ChangeUser.vue';
import DatabaseRow from './DatabaseRow.vue';

defineProps({
    contents: {
        type: Object,
        required: true
    },
    name: {
        type: String,
        required: true
    },
    fieldOrder: {
        type: Array,
        required: true
    }
});
const newUserOverlay = ref(false);

function toggleOverlay(event, a){
    console.log(a)
    console.log(event.target.id)
    event.target.id === a ?  this.newUserOverlay = false : this.newUserOverlay = true
}

</script>

<template>
    <h1> {{ name }}</h1>
    <button id="overlay-button" @click="toggleOverlay($event)">
        Add user
    </button>
    <ChangeUser id="new-user-div" v-show="newUserOverlay" @click="toggleOverlay($event, 'new-user-div')" />
    <table>
        <th v-for="(field) in this.fieldOrder" :key="field">
            {{ field }}
        </th>
        <DatabaseRow v-for="(values) in contents" :fields="values" :fieldOrder="fieldOrder" :key="values.user_id"/>
    </table>
</template>