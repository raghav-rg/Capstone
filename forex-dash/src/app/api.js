// import axios from "axios";

// axios.defaults.baseURL =  'http://localhost:5000/api';

// const response = (resp) => resp.data;

// const requests = {
//     get: (url) => axios.get(url).then(response)
// }

// const endPoints = {
//     account: () => requests.get("/account"),
//     headlines: () => requests.get("/headlines"),
//     options: () => requests.get("/options"),
//     technicals: (p,g) => requests.get(`/technicals/${p}/${g}`),
//     prices: (p,g,c) => requests.get(`/prices/${p}/${g}/${c}`)
// }

// export default endPoints;

import axios from "axios";

axios.defaults.baseURL = 'http://localhost:5000/api';

const response = (resp) => resp.data;

const requests = {
    get: (url) => axios.get(url).then(response),
    post: (url) => axios.post(url).then(response) // Add support for POST requests
}

const endPoints = {
    account: () => requests.get("/account"),
    headlines: () => requests.get("/headlines"),
    options: () => requests.get("/options"),
    technicals: (p, g) => requests.get(`/technicals/${p}/${g}`),
    prices: (p, g, c) => requests.get(`/prices/${p}/${g}/${c}`),
    runBot: () => requests.post("/run-bot") // Add the run-bot endpoint
}

export default endPoints;
