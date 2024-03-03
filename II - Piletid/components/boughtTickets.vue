<template>
  <div class="flex flex-col max-w-[75rem]">
    <div class="-m-1.5 overflow-x-auto">
      <div class="p-1.5 min-w-full inline-block align-middle">
        <div class="overflow-hidden">
          <table
            class="min-w-full divide-y divide-gray-200 dark:divide-gray-700"
          >
            <thead>
              <tr>
                <th
                  scope="col"
                  class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                >
                  Lähtepeatus
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                >
                  Sihtpeatus
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                >
                  Stardiaeg
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                >
                  Kohalejõudmise aeg
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                >
                  Kuupäev
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-end text-xs font-medium text-gray-500 uppercase"
                >
                  Transpordivahend
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-end text-xs font-medium text-gray-500 uppercase"
                >
                  Hind
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
              <tr v-for="ticket in tickets">
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-gray-800 dark:text-gray-200"
                >
                  {{ ticket.from }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-gray-800 dark:text-gray-200"
                >
                  {{ ticket.to }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-gray-800 dark:text-gray-200"
                >
                  {{ ticket.start_time }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-gray-800 dark:text-gray-200"
                >
                  {{ ticket.end_time }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-gray-800 dark:text-gray-200"
                >
                  {{ ticket.date }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-gray-800 dark:text-gray-200"
                >
                  {{ ticket.vehicle_type }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-gray-800 dark:text-gray-200"
                >
                  {{ ticket.price }}€
                </td>
                
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const supabase = useSupabaseClient();
const purchases = ref([]);
const tickets = ref([]);
const ticketIDs = ref([]);

async function getPurchases() {
  const { data } = await supabase.from("purchases").select();
  purchases.value = data;
  bigData(purchases);
}
function bigData(purchases) {
  purchases.value.forEach((purchase) => {
    ticketIDs.value.push(purchase.ticket_id);
  });
  getTicketInfo(ticketIDs);
}
async function getTicketInfo(ticketIDs) {
  const { data } = await supabase
    .from("tickets")
    .select()
    .in("ticket_id", ticketIDs.value);
  tickets.value = data;
  //console.log(tickets.value);
  duplicateTickets();
}
function duplicateTickets() {
  // Count occurrences of each ticketID
  const ticketIDCounts = ticketIDs.value.reduce((acc, id) => {
    acc[id] = (acc[id] || 0) + 1;
    return acc;
  }, {});

  // Duplicate tickets with ticketID that have more than one occurrence
  const duplicatedTickets = tickets.value.reduce((acc, ticket) => {
    const count = ticketIDCounts[ticket.ticket_id];
    if (count > 1) {
      for (let i = 0; i < count; i++) {
        acc.push(ticket);
      }
    } else {
      acc.push(ticket);
    }
    return acc;
  }, []);

  tickets.value = duplicatedTickets;
}

onMounted(() => {
  getPurchases();
});
</script>
