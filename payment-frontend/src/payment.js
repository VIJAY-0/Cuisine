import React from "react";
import axios from "axios";

const Payment = () => {
    const handlePayment = async () => {
        const { data: order } = await axios.get('/payment/initiate/');
        const options = {
            key: 'RAZORPAY_KEY', // Replace with Razorpay key
            amount: order.amount,
            currency: order.currency,
            name: 'CUISINE',
            description: 'Test Transaction',
            order_id: order.id,
            handler: (response) => {
                axios.post('/payment/verify/', response)
                     .then(() => alert('Payment successful!'))
                     .catch(() => alert('Payment failed.'));
            },
        };
        const rzp = new window.Razorpay(options);
        rzp.open();
    };

    return (
        <div>
            <h2>Payment Page</h2>
            <button onClick={handlePayment}>Pay Now</button>
        </div>
    );
};

export default Payment;
