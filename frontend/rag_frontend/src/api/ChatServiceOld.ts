// import { DefaultApi, Configuration } from "../api-client"; // Import the generated API client
// import { SubmitQueryRequest, DBQueryModel } from "../api-client"; // Correct imports

// // Configure the base URL for your API
// const config = new Configuration({
//   basePath: "http://localhost:8000", // Set the correct base URL
// });
// const api = new DefaultApi(config);

// // Fetch previous conversations for a user
// export const getPreviousConversations = async (
//   userId: string,
// ): Promise<DBQueryModel[]> => {
//   try {
//     const response = await api.listQueryEndpointListQueriesGet({ userId });
//     return response; // Returns an array of DBQueryModel
//   } catch (error) {
//     console.error("Error fetching previous conversations:", error);
//     throw error;
//   }
// };

// // Service function to submit the query
// export const submitQuery = async (
//   username: string,
//   queryText: string,
// ): Promise<string> => {
//   const requestBody: SubmitQueryRequest = {
//     queryText: queryText,
//     userId: username, // Pass username instead of hardcoded user ID
//   };

//   try {
//     const result = await api.submitQueryEndpointSubmitQueryPost({
//       submitQueryRequest: requestBody,
//     });
//     return result.answerText || ""; // Return the bot's response (answerText)
//   } catch (error) {
//     console.error("Error submitting query:", error);
//     throw error;
//   }
// };
