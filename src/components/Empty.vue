<template>
  <div class="empty">
    <slot>
      <p>No Data.</p>
    </slot>
  </div>
</template>

<script setup lang="ts"></script>

<style>
.empty {
  @apply
    grid
    rounded-md
    bg-slate-700
    p-2
    text-center
    place-content-center
    place-items-center
    gap-2;
}
</style>
