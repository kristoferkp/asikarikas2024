<template>
  <div class="max-w-6xl py-10 px-4 sm:px-6 lg:px-8 lg:py-16 mx-auto">
    <div class="max-w-xl text-center mx-auto">
      <div class="mb-5">
        <h2
          class="text-2xl font-bold md:text-3xl md:leading-tight dark:text-white"
        >
          Kontrolli oma piletit
        </h2>
      </div>

      <form @submit.prevent="checkTicket">
        <div
          class="mt-5 lg:mt-8 flex flex-col items-center gap-2 sm:flex-row sm:gap-3"
        >
          <div class="w-full">
            <input
              type="text"
              id="ticket"
              name="ticket"
              class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
              placeholder="Lisa oma pileti number"
            />
          </div>
          <input
            type="submit"
            :value="loading ? 'Laeb' : 'Kontrolli'"
            :disabled="loading"
            class="max-w-sm py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-gradient-to-tl from-blue-600 to-violet-600 hover:from-violet-600 hover:to-blue-600 text-white disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
          />
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
const supabase = useSupabaseClient();

const loading = ref(false);

async function checkTicket(event) {
  console.log("checkTicket");
  event.preventDefault();
  const value = document.getElementById("ticket").value;
  const { data, error } = await supabase
    .from("purchases")
    .select("*")
    .eq("purchase_id", value);
  if (error) {
    alert("Viga pileti kontrollimisel");
  } else if (data.length === 0) {
    alert(`Vale pileti number: ${value}`);
  } else {
    alert(`Õige pileti number: ${value}`);
  }
}
</script>
