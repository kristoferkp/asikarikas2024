<script setup>
const supabase = useSupabaseClient();

const loading = ref(true);
const username = ref("");
const website = ref("");
const avatar_path = ref("");
const purchases = ref([]);

loading.value = true;
const user = useSupabaseUser();

const { data } = await supabase
  .from("profiles")
  .select(`username, website, avatar_url`)
  .eq("id", user.value.id)
  .single();

if (data) {
  username.value = data.username;
  website.value = data.website;
  avatar_path.value = data.avatar_url;
}

loading.value = false;

async function updateProfile() {
  try {
    loading.value = true;
    const user = useSupabaseUser();

    const updates = {
      id: user.value.id,
      username: username.value,
      website: website.value,
      avatar_url: avatar_path.value,
      updated_at: new Date(),
    };

    const { error } = await supabase.from("profiles").upsert(updates, {
      returning: "minimal", // Don't return the value after inserting
    });

    if (error) throw error;
  } catch (error) {
    alert(error.message);
  } finally {
    loading.value = false;
  }
}

async function signOut() {
  try {
    loading.value = true;
    const { error } = await supabase.auth.signOut();
    if (error) throw error;
  } catch (error) {
    alert(error.message);
  } finally {
    loading.value = false;
  }
}

async function getPurchases() {
  const { data } = await supabase.from("purchases").select();
  purchases.value = data;
}
onMounted(() => {
  getPurchases();
});
</script>

<template>
  <div class="max-w-[85rem] mx-auto flex-auto">
    <!-- Grid -->
    <div class="">
      <form class="grid md:grid-cols-4" @submit.prevent="updateProfile">
        <Avatar v-model:path="avatar_path" @upload="updateProfile" />
        <div class="max-w-md">
          <div class="p-1">
            <label
              for="hs-leading-icon email"
              class="block text-sm font-medium mb-2 dark:text-white"
              >Emaili aadress</label
            >
            <div class="relative">
              <input
                type="text"
                :value="user.email"
                id="hs-leading-icon"
                name="hs-leading-icon"
                class="py-3 px-4 ps-11 block w-full border-gray-200 shadow-sm rounded-lg text-sm focus:z-10 focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                placeholder="example@example.com"
              />
              <div
                class="absolute inset-y-0 start-0 flex items-center pointer-events-none z-20 ps-4"
              >
                <svg
                  class="flex-shrink-0 size-4 text-gray-400 dark:text-gray-600"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <rect width="20" height="16" x="2" y="4" rx="2" />
                  <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7" />
                </svg>
              </div>
            </div>
          </div>
          <div class="p-1">
            <label
              for="hs-leading-icon username"
              class="block text-sm font-medium mb-2 dark:text-white"
              >Kasutajanimi</label
            >
            <div class="relative">
              <input
                type="text"
                v-model="username"
                id="hs-leading-icon username"
                name="hs-leading-icon"
                class="py-3 px-4 ps-11 block w-full border-gray-200 shadow-sm rounded-lg text-sm focus:z-10 focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                placeholder="Kasutajanimi"
              />
              <div
                class="absolute inset-y-0 start-0 flex items-center pointer-events-none z-20 ps-4"
              >
                <svg
                  class="flex-shrink-0 size-4"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2" />
                  <circle cx="12" cy="7" r="4" />
                </svg>
              </div>
            </div>
          </div>
        </div>
        <div class="max-w-md">
          <div class="p-5">
            <button
              type="submit"
              class="w-full mt-3 py-2 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
              :value="loading ? 'Laeb ...' : 'Uuenda'"
              :disabled="loading"
            >
              Uuenda
            </button>
          </div>

          <div class="p-5">
            <button
              type="button"
              @click="signOut"
              :disabled="loading"
              class="w-full mt-1 py-2 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
            >
              Logi välja
            </button>
          </div>
        </div>
        <div>
          <p class="block text-sm font-medium mb-2 dark:text-white">
            Ostetud Piletid
          </p>
          <ul>
            <li
              class="w-full mt-1 py-2 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
              v-for="purchase in purchases"
              :key="purchase.id"
            >
              {{ purchase.purchase_id }}
            </li>
          </ul>
        </div>
      </form>
    </div>
    <BoughtTickets />
  </div>
</template>
