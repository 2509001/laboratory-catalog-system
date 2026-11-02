import { getEquipment } from "../services/api.js";

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
                    <th>Name</th>
                    <th>Brand</th>
                    <th>Model</th>
                    <th>Status</th>
                </tr>
            </thead>

            <tbody id="equipment-body">
                ${equipment.map(item => `
                    <tr>
                        <td>${item.name}</td>
                        <td>${item.brand ?? ""}</td>
                        <td>${item.model ?? ""}</td>
                        <td>${item.operational_status}</td>
                    </tr>
                `).join("")}
            </tbody>

        </table>
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
                    <td>${item.name}</td>
                    <td>${item.brand ?? ""}</td>
                    <td>${item.model ?? ""}</td>
                    <td>${item.operational_status}</td>
                </tr>
            `).join("");

    });

}