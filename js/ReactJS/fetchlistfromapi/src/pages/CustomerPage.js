import React, { useState, useEffect } from "react";

const CustomerPage = () => {
  const [customerList, setCustomerList] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        fetch("https://jsonplaceholder.typicode.com/users")
          .then((response) => response.json())
          .then((data) => {
            setCustomerList(data);
          });
        setIsLoading(false);
      } catch (error) {
        console.log(error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {isLoading ? (
            <tr>
              <td>Data isLoading......</td>
            </tr>
          ) : (
            customerList &&
            customerList.map((customer) => {
              return (
                <tr key={customer.id}>
                  <td>{customer.id}</td>
                  <td>{customer.name}</td>
                </tr>
              );
            })
          )}
        </tbody>
      </table>
    </div>
  );
};

export default CustomerPage;
