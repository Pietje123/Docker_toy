<script setup>
import { ref, onBeforeMount, onMounted } from 'vue'
import DatabaseTable from './DatabaseTable.vue'
import ChangeUser from './ChangeUser.vue'

defineProps({
  dbTables: String
})

let dbTables = ref("")

function loadDatabase() {
  fetch('/api/').then(
        async (res) => {
            const data = await res.json();
            dbTables.value = data.results;
        }
    )
};


function newUser(values) {
  const requestOptions =  {
    method : 'POST', 
    headers: {
      "Content-Type": "application/json",
    },

    body : JSON.stringify(values),
  };
  fetch('/api/new_user/', requestOptions).then( async response => {
      const res = await response;
    }
  ).then(() => loadDatabase())
}
onBeforeMount(() => {
  loadDatabase()
})
</script>

<template>
  <div class="db">
    <DatabaseTable v-for="(table, name) in dbTables" :contents="table" :name="name" :fieldOrder="['username', 'birthdate']"/>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
