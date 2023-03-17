<template>
  <div class="list">
    <ul class="list-items">
      <li v-for="item in items" :key="item.id">
        <h3>{{ item.weapon }}</h3>
        <div>Tier: {{ item.tier }}</div>
        <div>Skill: {{ item.skill }}</div>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
defineProps({
  items: {
    type: Object,
    required: false,
  },
})
</script>

<style scoped>
.list {

}

.list-items {
  @apply
    flex
    flex-col
    gap-2
    lg:grid
    lg:grid-cols-2
    xl:grid-cols-3
    xl:gap-4;
}

.list-items h3 {
  @apply
    text-xl
    lg:text-2xl
    mb-2
    lg:mb-4;
}

.list-items > li {
  @apply
    p-4
    xl:p-6
    rounded-md
    bg-slate-200;
}
</style>