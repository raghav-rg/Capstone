import React, { useEffect, useState } from 'react';
import endPoints from '../app/api';
import TitleHead from './TitleHead';

const DATA_KEYS = [
    { name: "Account ID", key: "Id" },
    { name: "Accounting Type", key: "AccountingType" },
    { name: "Name", key: "Name" },
    { name: "Email", key: "Email" },
    { name: "Registered", key: "Registered" },
    { name: "Modified", key: "Modified" },
    { name: "Leverage", key: "Leverage" },
    { name: "Balance", key: "Balance" },
    { name: "Balance Currency", key: "BalanceCurrency" },
    { name: "Profit", key: "Profit" },
    { name: "Commission", key: "Commission" },
    { name: "Agent Commission", key: "AgentCommission" },
    { name: "Swap", key: "Swap" },
    { name: "Rebate", key: "Rebate" },
    { name: "Equity", key: "Equity" },
    { name: "Margin", key: "Margin" },
    { name: "Margin Call Level", key: "MarginCallLevel" },
    { name: "Stop Out Level", key: "StopOutLevel" },
    { name: "Report Currency", key: "ReportCurrency" },
]

function AccountSummary() {
    const [account, setAccount] = useState(null);

    useEffect(() => {
        loadAccount();
    }, []);

    const loadAccount = async () => {
        const data = await endPoints.account();
        setAccount(data);
    }

    return (
        <div>
            <TitleHead title="Account Summary" />
            {
                account && <div className='segment'>
                    {
                        DATA_KEYS.map(item => {
                            return <div key={item.key} className="account-row">
                                <div className='bold header'>{item.name}</div>
                                <div>{account[item.key]}</div>
                            </div>
                        })
                    }
                </div>
            }
        </div>
    );
}

export default AccountSummary;
