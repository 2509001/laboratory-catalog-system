import {
    getEquipment,
    updateEquipmentStatus
} from "../services/api.js";

export async function renderEquipmentCatalog() {

    const equipment = await getEquipment();

    return `
        <h1>Equipment Catalog</h1>

        <input
            type="text"
            id="search"
            placeholder="Search equipment..."
        />

        <br><br>

        <table border="1">

            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Brand</th>
                    <th>Model</th>
                    <th>Status</th>
                </tr>
            </thead>

            <tbody id="equipment-body">

                ${equipment.map(item => `
                    <tr>
                        <td>${item.equipment_id}</td>
                        <td>${item.name}</td>
                        <td>${item.brand ?? ""}</td>
                        <td>${item.model ?? ""}</td>
                        <td>${item.operational_status}</td>
                    </tr>
                `).join("")}

            </tbody>

        </table>

        <br><br>

        <h2>Update Equipment Status</h2>

        <input
            type="text"
            id="equipment-id"
            placeholder="Equipment ID"
        />

        <select id="equipment-status">
            <option>Operational</option>
            <option>Under Maintenance</option>
            <option>Out of Service</option>
            <option>Reserved</option>
        </select>

        <button id="update-status">
            Update Status
        </button>

        <p id="status-message"></p>
    `;
}

export async function setupSearch() {

    const equipment = await getEquipment();

    const searchInput =
        document.getElementById("search");

    searchInput.addEventListener("input", () => {

        const value =
            searchInput.value.toLowerCase();

        const filtered = equipment.filter(item =>

            item.name?.toLowerCase().includes(value) ||

            item.brand?.toLowerCase().includes(value) ||

            item.model?.toLowerCase().includes(value)

        );

        document.getElementById("equipment-body")
            .innerHTML = filtered.map(item => `
                <tr>
                    <td>${item.equipment_id}</td>
                    <td>${item.name}</td>
                    <td>${item.brand ?? ""}</td>
                    <td>${item.model ?? ""}</td>
                    <td>${item.operational_status}</td>
                </tr>
            `).join("");

    });

}

export function setupStatusUpdate() {

    const button =
        document.getElementById("update-status");

    button.addEventListener("click", async () => {

        const equipmentId =
            document.getElementById("equipment-id").value;

        const status =
            document.getElementById("equipment-status").value;

        const result =
            await updateEquipmentStatus(
                equipmentId,
                status
            );

        document.getElementById(
            "status-message"
        ).textContent =
            result.message;

    });

}