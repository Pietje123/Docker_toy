<script setup>

defineProps({
    fields: {
        type: Object,
        required: true
    },
});
</script>
<template>
    <h1 v-for="field in fields">
        {{ field }}
    </h1>
</template>