<template>
  <div class="pagination">
    <div>
      <button
        class="btn sm"
        :disabled="prevDisabled"
        @click="prevPage"
      >
          &larr;
      </button>
    </div>
    <div>
      <p>{{ pagePlace }}</p>
    </div>
    <div>
      <button
        class="btn sm"
        :disabled="nextDisabled"
        @click="nextPage"
      >
          &rarr;
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  pageNumber: {
    type: Number,
    required: true,
  },
  pageCount: {
    type: Number,
    required: true,
  },
})

const emit = defineEmits(['next-page', 'prev-page'])

const pagePlace = computed(() => {
  return `Page ${props.pageNumber + 1} of ${props.pageCount}`
})

const prevDisabled = computed(() => {
  return !(props.pageNumber > 0)
})

const nextDisabled = computed(() => {
  return !(props.pageNumber < props.pageCount -1)
})

const prevPage = () => {
  emit('prev-page')
}

const nextPage = () => {
  emit('next-page')
}
</script>

<style scoped>
.pagination {
  @apply
    flex
    items-center
    justify-center
    gap-4;
}
</style>