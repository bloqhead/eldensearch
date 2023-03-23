<template>
  <div class="loading">
    <div class="wrapper">
      <div class="icon">
        <fa :icon="['fasr', 'skull']" spin />
      </div>
      <div class="content">
        <slot>
          <p>Loading</p>
        </slot>
        <div v-if="expired">
          <button
            class="btn mt-4"
            @click="reload()"
          >
            Reload
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue'
import type { Ref } from 'vue'

const emit = defineEmits(['loading-expired', 'retry'])

const expired: Ref = ref<Boolean>(false)
const timeout: Ref = ref<Number>(3000)

const giveWarning = () => {
  setTimeout(() => {
    expired.value = true
  }, timeout.value)
}

const reload = () => {
  emit('retry')
  
  expired.value = false

  nextTick(() => {
    giveWarning()
  })
}

onMounted(() => {
  giveWarning()
})
</script>

<style>
.loading {
  @apply
    block
    text-center
    text-slate-400
    overflow-visible;
}

.loading .wrapper {
  @apply
    inline-flex
    flex-col
    gap-4
    rounded-md
    bg-slate-800
    p-8
    my-4
    divide-y
    divide-slate-600
    shadow-md;
}

.loading .icon {
  @apply text-5xl;
}

.loading .content {
  @apply 
    text-sm
    uppercase
    tracking-widest
    pt-2
    px-2;
}
</style>